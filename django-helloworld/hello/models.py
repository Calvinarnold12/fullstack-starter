from django.db import models
from django.contrib.auth.models import User

# 1. Player Profile (Extends the default Django User for stats)
class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_games_played = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)

    def win_percentage(self):
        if self.total_games_played == 0:
            return 0
        return round((self.total_wins / self.total_games_played) * 100, 1)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# 2. Game Variant (Keeps track of Polymorphic games like Klondike vs Spider)
class GameVariant(models.Model):
    name = models.CharField(max_length=50, unique=True) # e.g., "Klondike", "FreeCell"
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# 3. Game Session (Records individual game history and states)
class GameSession(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game_variant = models.ForeignKey(GameVariant, on_delete=models.CASCADE)
    
    # Timing and Status
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_won = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    
    # This will let you save the exact state of the cards if they leave midway!
    game_state = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.player.username} playing {self.game_variant.name} on {self.start_time.strftime('%Y-%m-%d')}"