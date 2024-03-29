from dataclasses import dataclass
import pygame, pytmx, pyscroll

from src.player import NPC


@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str
    npcs: list[NPC]

@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]

class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()
        self.screen = screen
        self.player = player
        self.current_map = "world"

        self.register_map("world", portals=[
            Portal(from_world="world", origin_point="enter_house1", target_world="house1", teleport_point="spawn_house1"),
            Portal(from_world="world", origin_point="enter_house2", target_world="house2",teleport_point="spawn_house2")
        ], npcs=[
            NPC('paul', nb_points=11),
            NPC('robin', nb_points=16)
        ])
        self.register_map("house1", portals=[
            Portal(from_world="house1", origin_point="exit_house1", target_world="world", teleport_point="enter_house1_exit")
        ])
        self.register_map("house2", portals=[
            Portal(from_world="house2", origin_point="exit_house2", target_world="world", teleport_point="enter_house2_exit")
        ])
        self.teleport_player("player")
        self.teleport_npcs()

    def check_collision(self):
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)

        for sprite in self.get_group().sprites():

            if type(sprite) is NPC:
                if sprite.feet.collidelist(self.player.rect):
                    sprite.speed =0
                else:
                    sprite.speed = 1

            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[], npcs=[]):
        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"../map/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2.5

        # definir une liste pour stocker les collisions
        walls = []
        for obj in tmx_data.objects:
            if obj.name == 'collision':
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        group.add(self.player)

        # recuperer tout les npcs
        for npc in npcs:
            group.add(npc)

        # creer un obj map
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_onject_by_name(name)

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collision()

        for npc in self.get_map().npcs:
            npc.move()