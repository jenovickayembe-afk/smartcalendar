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
    
# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

class UserDTO:
    def __init__(self, id, email, role, google_linked):
        self.id = id
        self.email = email
        self.role = role
        self.google_linked = google_linked

class EtudiantDTO:
    def __init__(self, id_etudiant, matricule, nom, prenom, email, id_promotion=None):
        self.id_etudiant = id_etudiant
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.id_promotion = id_promotion


class EnseignantDTO:
    def __init__(self, id_enseignant, nom, prenom, email):
        self.id_enseignant = id_enseignant
        self.nom = nom
        self.prenom = prenom
        self.email = email


class PromotionDTO:
    def __init__(self, id_promotion, nom_promo, annee_academique):
        self.id_promotion = id_promotion
        self.nom_promo = nom_promo
        self.annee_academique = annee_academique


class UniteEnseignementDTO:
    def __init__(self, id_ue, code_ue, intitule, credits_ects):
        self.id_ue = id_ue
        self.code_ue = code_ue
        self.intitule = intitule
        self.credits_ects = credits_ects

class CoursDTO:
    def __init__(self, id_cours, intitule_cours, volume_horaire, id_ue):
        self.id_cours = id_cours
        self.intitule_cours = intitule_cours
        self.volume_horaire = volume_horaire
        self.id_ue = id_ue


class SeanceDTO:
    def __init__(self, id_seance, titre, date, heure_debut, heure_fin, salle, statut_synchro, type, id_cours=None):
        self.id_seance = id_seance
        self.titre = titre
        self.date = date
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.salle = salle
        self.statut_synchro = statut_synchro
        self.type = type
        self.id_cours = id_cours


class NotificationDTO:
    def __init__(self, id_notification, message, date_envoi):
        self.id_notification = id_notification
        self.message = message
        self.date_envoi = date_envoi

# Avec Python, les class Interfaces peuvent être implémentées comme des classes abstraites
# heritant de Protocol
import sqlite3
from random import randint
from typing import List, Optional, Protocol

from Models import EnseignantDTO, EtudiantDTO, UserDTO


class DAO:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup_db()

    def _setup_db(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            role TEXT,
            email TEXT,
            logedin BOOLEAN
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS promotions (
            id_promotion INTEGER PRIMARY KEY,
            nom_promo TEXT NOT NULL,
            annee_academique TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS etudiants (
            id_etudiant INTEGER PRIMARY KEY,
            matricule TEXT NOT NULL,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL,
            id_promotion INTEGER,
            FOREIGN KEY (id_promotion) REFERENCES promotions(id_promotion)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS enseignants (
            id_enseignant INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS unites_enseignement (
            id_ue INTEGER PRIMARY KEY,
            code_ue TEXT NOT NULL,
            intitule TEXT NOT NULL,
            credits_ects INTEGER NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cours (
            id_cours INTEGER PRIMARY KEY,
            intitule_cours TEXT NOT NULL,
            volume_horaire INTEGER NOT NULL,
            id_ue INTEGER,
            FOREIGN KEY (id_ue) REFERENCES unites_enseignement(id_ue)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS seances (
            id_seance INTEGER PRIMARY KEY,
            titre TEXT NOT NULL,
            date TEXT NOT NULL,
            heure_debut TEXT NOT NULL,
            heure_fin TEXT NOT NULL,
            salle TEXT,
            statut_synchro TEXT,
            type TEXT NOT NULL,
            id_cours INTEGER,
            FOREIGN KEY (id_cours) REFERENCES cours(id_cours)
        )
        """)

        self.conn.commit()




class BaseDAO(Protocol):
    def get_by_id(self, id):
        pass

    def get_all(self):
        pass

    def save(self, obj):
        pass

    def delete(self, id):
        pass





class UserDAO(DAO):
    def __init__(self):
        super().__init__()

    def get_by_id(self, id) -> UserDTO:
        pass

    def get_all(self) -> list[UserDTO]:
        pass

    def save(self, user: UserDTO) -> None:
        pass

    def delete(self, id: int) -> None:
        pass

    def get_by_email(self, email) -> UserDTO:
        pass



class EtudiantDAO(DAO):
    def __init__(self):
        super().__init__()

    def get_by_id(self, id) -> EtudiantDTO:
        pass

    def get_all(self) -> list[EtudiantDTO]:
        pass

    def save(self, etudiant: EtudiantDTO) -> None:
        pass

    def delete(self, id: int) -> None:
        pass

    def get_by_promotion(self, promotion_id) -> list[EtudiantDTO]:
        pass





class EnseignantDAO(DAO):
    def __init__(self):
        super().__init__()

    def get_by_id(self, id) -> EnseignantDTO:
        pass

    def get_all(self) -> list[EnseignantDTO]:
        pass

    def save(self, enseignant: EnseignantDTO) -> None:
        pass

    def delete(self, id_enseignant) -> None:
        pass

    def get_by_ue(self, ue_id) -> list[EnseignantDTO]:
        pass




class PromotionDAO(DAO):
    def __init__(self):
        super().__init__()



class EventDAO(DAO):
    def __init__(self):
        super().__init__()