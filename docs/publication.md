# Contrat de séparation et de publication

| Dépôt | GitHub | Contenu | Export public |
| --- | --- | --- | --- |
| bringmeback-okf | public | contrat, outils, modèles anonymes | oui |
| bringmeback-content | privé au lancement | faits publiables, expériences de ville générales, médias autorisés | uniquement liste blanche après révision |
| bringmeback-private | privé durablement | lieux libertins, avis intimes, notes non publiées, ressources de rencontres | **jamais de synchronisation automatique** |

Règle absolue : les deux dépôts potentiellement publics **ne connaissent aucun ID privé**. Les extensions privées peuvent citer l'ID d'un lieu public via `extends` (ex. commentaire privé sur un bar ordinaire), sans recopier sa fiche.

Pipeline recommandé : (1) PR de contenu, (2) vérification des champs/IDs et contrôle des données personnelles, (3) approbation éditoriale explicite, (4) export en **liste blanche de champs** depuis content seulement, (5) publication WordPress/Astro. Pour publier un extrait intime déjà assumé dans un article ABDD, le rédiger/valider explicitement comme un nouveau texte public ; **ne jamais exporter le document privé source**.

Ne pas compter sur `.gitignore` pour effacer un secret commité : les historiques Git conservent les versions. Accès GitHub au dépôt privé = accès pour ses collaborateurs, non chiffrement de bout en bout. Retirer EXIF géographiques et données de tiers des médias approuvés. Aucune authentification, conversation ni profil humain détaillé dans ce référentiel.
