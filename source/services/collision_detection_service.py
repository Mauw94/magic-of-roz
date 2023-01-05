import arcade

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from views.game_view import GameView
    
class CollisionDetectionService:
    
    def collision_detection(self, game: 'GameView'):
        self.__coins_collision_detection(game)
        self.__bullet_collision_detection(game)
        
    def __coins_collision_detection(self, game: 'GameView'):
        coin_hit_list = arcade.check_for_collision_with_list(
            game.player, game.scene["Coins"])
        for coin in coin_hit_list:
            game.score += 1
            print("current score: ", game.score)
            coin.remove_from_sprite_lists()
            arcade.play_sound(game.coin_collect_sound)
    
    def __bullet_collision_detection(self, game: 'GameView'):
        for bullet in game.scene["Bullets"]:
            bullet_hit_list = arcade.check_for_collision_with_list(bullet, game.scene["Enemies"])
            if bullet_hit_list:
                bullet.remove_from_sprite_lists()
                for enemy in bullet_hit_list:
                    enemy.health -= game.player.normal_ranged_attack_dmg
                    
                    if enemy.health <= 0:
                        enemy.remove_from_sprite_lists()
                    
                    arcade.play_sound(game.normal_hit_sound)
