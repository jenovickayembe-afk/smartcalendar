# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml
class UserDAO:
    def __init__(
        self,
    ):
        pass


class EventDAO:
    def __init__(
        self,
    ):
        pass
#Exercice 1

from data import UserDTO, EtudiantDTO, CoursDTO, SeanceDTO, EnseignantDTO

class BaseDAO:
    def __init__(
            self,  ):
                    pass
    def get_by_id(self, id)-> UserDTO:
        pass
    def get_all(self) -> list:
        pass
    def save(self, obj) -> None:
        pass
    def delete(self, id) -> None:
        pass


class UserDAO:
    def __int__(
                sefl, ):
          pass
    def get_by_email(self, email) -> UserDTO:
        pass
    def upadate_token( sefl, user_id, token) -> None:
        pass
    def save(self, obj) -> None:
        pass
    def delet(self, id) -> None:
        pass
    def get_by_email(self, email) -> UserDTO:
        pass
    def update_token(self, user_id: int, token: str) -> UserDTO:
         pass
class EtudiantDAO:
    def __int__(
               self, ):
        pass
    def get_by_promotion(self, id_promo) -> EtudiantDTO:
        pass    
    def get_all(self) -> list[EtudiantDTO]:
        pass
    
