# Mode d'emploi du dépôt

## Emplacements

| Répertoire | Contenu | Règle |
| --- | --- | --- |
| `course/` | Consignes, cours, notes et fiches d'examen reçus | Référence pédagogique ; conserver les originaux. |
| `sources/primary/` | Documents TotalEnergies ou institutionnels originaux | Nom stable, date et provenance dans `sources/register.md`. |
| `sources/benchmark/` | Documents concurrents, études sectorielles et benchmarks originaux | Même traçabilité ; distinguer communiqué et résultat mesuré. |
| `sources/synthesis/` | Synthèses factuelles d'un corpus ou d'une question | Utiliser `spec-kit/source_synthesis.md` ; jamais une source primaire. |
| `work/research/` | Notes d'enquête, vérifications, questions ouvertes | Travail intermédiaire. |
| `work/options/` | Diagnostics concurrents, idées retenues/rejetées, arbitrages | Raisonnement de l'équipe. |
| `work/projects/` | Liste longue, fiches projet et portefeuille | Une fiche par projet vedette ; autres projets plus courts. |
| `work/finance/` | Hypothèses, modèle et contrôles de calcul | Réconcilier avec les fiches et le rapport. |
| `deliverables/report/`, `memo/`, `slides/` | Versions prêtes à remettre | Numéros de version et même base de chiffres. |
| `deliverables/archive/` | Copie immuable des fichiers envoyés | Date et heure de remise. |

`work/roadmap.md` pilote le travail. `work/legacy_plan_unverified.md` est un ancien brouillon à auditer. Les dossiers vides n'ont pas besoin de fichier de remplissage : ils apparaîtront dans Git avec leur premier contenu.

## Noms et traçabilité

- Fichiers de travail : `sujet_court.md` ; synthèses : `YYYY-MM-DD_sujet.md` ; sources originales : conserver un nom reconnaissable, ajouter l'année si nécessaire.
- Chaque synthèse cite les documents d'origine, les pages ou sections et les liens exacts. Inscrire chaque source retenue dans `sources/register.md`.
- Dans les notes et livrables, marquer les énoncés `Fait`, `Calcul`, `Hypothèse`, `Observation locale` ou `Inconnu` jusqu'à la révision éditoriale finale. Une hypothèse chiffrée donne sa formule et son intervalle plausible.
- Les sorties de Perplexity ou d'autres IA externes sont des pistes de recherche. Vérifier les liens et lire les sources originales avant de reprendre une affirmation.

## Kit et issues

`spec-kit/` contient les gabarits de synthèse, de fiche projet et d'issue. `prompts/` contient des instructions prêtes à copier dans des IA externes, spécialisées par question. Une issue GitHub correspond à une ligne de la roadmap et possède un label de livrable (`dossier`, `memo`, `slides`, etc.), un responsable et un critère de fin. Ne pas cocher une tâche parce qu'un texte existe : la preuve et la cohérence doivent être vérifiées.
