# Contrat BringMeBack / profil voyage 1.0.0

## Formats et compatibilité
Markdown UTF-8 + frontmatter YAML délimité par `---`. La cible de compatibilité historique est `okf_version: "0.2"` ; le schéma métier **spécifique à BringMeBack** est `x-bringmeback.version: "1.0.0"`. Le dépôt initial ne contenait aucune définition normative de « OKF V2 » ; ce profil constitue donc une proposition locale versionnée, non une certification par un organisme extérieur.

## Familles
`destination` (pays/ville), `place` (adresse/lieu), `visit` (passage daté ou période inconnue), `experience` (vécu/persona non identifiants), `resource` (plateforme de préparation), `collection` (ensemble de références), `article` (publication), `note` (observations en attente), `overlay` (extension de données publiques).

Les noms/IDs restent indépendants : **ne jamais recycler un ID**, même si le nom commercial change. Chaque lieu a un fichier propre. Les nouveaux commentaires entrent comme entrées datables en annexe ou notes séparées ; on ne réécrit pas silencieusement une expérience historique.

## Frontmatter minimal
```yaml
---
id: bmb:place:nl:amsterdam:rosalias-menagerie
kind: place
title: Rosalia’s Menagerie
slug: rosalias-menagerie
okf_version: "0.2"
x-bringmeback:
  version: "1.0.0"
access: public
sensitivity: ordinary
publication: review_required
status: active # historical | check_required | draft | active
country_code: NL
city: Amsterdam
tags: [cocktails]
source_ids: [bmb:source:amsterdam-abdd-2026]
fact_checked_at: null
visited_at: null
---
```

Les dates `null` signifient **non établies**, jamais la date du commit. `visited_at` ne doit pas être déduit d'une photo sans recoupement. `status: check_required` interdit de présenter horaires, existence et conditions d'accès comme actuels.

`access` exprime la frontière de stockage/publication. `sensitivity` décrit la nature du contenu. `publication` exprime son état de validation, distinct de `access`. Un dépôt privé ne transforme pas automatiquement chaque enregistrement en secret.

## Liens
Les relations utilisent l'ID stable et jamais un chemin relatif fragile. `extends` ne pointe que **privé → public**, jamais public → privé. Les lieux de Muiden, Zaandijk, Zaandam et Utrecht portent leurs véritables villes. Le carnet Amsterdam peut référencer une excursion vers Zaandam, sans déplacer Zaanse Schans.

## Propriété éditoriale et vérifications
Distinguer faits d'une source officielle, souvenirs de l'auteur, recommandation vécue, avis non testé. Conserver `source_ids`, `fact_checked_at`, `visited_at`, et les notes horodatées lorsque la date est connue. Ne pas déduire d'avis actuels d'une visite ancienne. Ne jamais enregistrer noms de partenaires, pseudonymes, hôtels/chambres de rendez-vous, échanges privés, tokens, coordonnées de personnes ou images sans consentement.

## Évolution
Nouveau champ optionnel = changement mineur dans `x-bringmeback.version`. Modification cassante = version majeure et script de migration explicite. `okf_version` évolue séparément, sans écraser la source historique. Le pipeline doit valider schémas, unicité d'IDs, liens, permissions et projections publiques avant publication.
