# -*- coding: utf-8 -*-
from video import Video


class Movies(Video):
    '''Main class as template to create new movies'''
    if __name__ == "__main__":
        print("This shouldn´t be run as main program "
              "please use the entertainment_center.py file")

    def __init__(
            self, title, durration, storyline,
            poster_image_url, trailer_youtube_url):
        '''
        :param title: string
        :param durration: string
        :param storyline: string
        :param poster_image_url: string
        :param trailer_youtube_url: string
        '''
        Video.__init__(self, title, durration)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
