# -*- coding: utf-8 -*-
class Video():
    '''Parent class where common attributes getting
    stored so further classes can inherit from it'''
    if __name__ == "__main__":
        print("This shouldn´t be run as main program "
              "please use the entertainment_center.py file")

    def __init__(self, title, durration):
        '''
        :param title: string
        :param durration: string
        '''
        self.title = title
        self.durration = durration
