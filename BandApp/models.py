from django.db import models


class Post(models.Model):
    """This class will create a post

    Parameters:
        models.Model: model

    Attributes:
        song_title: Char
        song_lyrics: Text
        date_released: date
    """
    song_title = models.CharField(max_length=100)
    song_lyrics = models.TextField()
    date_released = models.DateField()
    
    def __str__(self):
        """This function returns the title of the song

        Parameters:
            self: Post object

        Returns:
            title: Char
        """
        return self.song_title