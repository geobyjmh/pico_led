STEP = 1
UP_DIRECTION = 1
DOWN_DIRECTION = -1

class position:
    def __init__(self, min_value, max_value):
        self.__min_value = min_value
        self.__max_value = max_value
        self.__direction = UP_DIRECTION
        self.__value = self.__min_value
        
    def get_value(self):
        self.__value += self.__direction * STEP
        
        if self.__value >= self.__max_value:
            self.__value = self.__max_value
            self.__direction = DOWN_DIRECTION
            
        if self.__value <= self.__min_value:
            self.__value = self.__min_value
            self.__direction = UP_DIRECTION
            
        return self.__value
            
        
            
            
        
        