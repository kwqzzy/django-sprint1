# gameparts/exceptions.py

class FieldIndexError(IndexError):


    def __init__(
        self,
        # Текст по умолчанию.
        message='Введено значение за границами игрового поля!'  
    ):
        super().__init__(message) 


class CellOccupiedError(Exception):
    

    def __init__(
            self,
            message='Попытка заменить занятую ячейку'
    ):
        

     super().__init__(message)