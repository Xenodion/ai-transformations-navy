# Préparation du Q&A : CEO sceptique, 5 minutes (deck v3, 16 novembre 2026)

**Statut :** préparation interne de l'équipe, pas un livrable. Les chiffres viennent de `work/finance/portfolio_model_working.xlsx` (feuilles Scenarios, Cash flow build, Half budget), de `deliverables/report/full_strategy_report.md` et des notes du deck. Les lignes marquées *[recalculé]* ont été recalculées le 15 nov. à partir des flux du workbook (impôt approximé à 25 %) ; elles ne figurent pas dans le rapport. À présenter comme « notre sensibilité », jamais comme des sorties du modèle montrées dans le deck.

**Format :** chaque réponse comprend une version orale de 20 secondes, les chiffres de soutien, et ce qu'il ne faut PAS dire. Réponse d'abord, preuves ensuite. Si un chiffre est une hypothèse, dire « hypothèse ».

---

## 0. Les cinq vraies brèches (à lire en premier)

| # | Brèche | Pourquoi un CEO affûté la trouve | Notre meilleure réponse |
|---|---|---|---|
| 1 | **« $2.90m at risk » minimise l'exposition.** Le Gate 0 (jour 90) est un gate de préparation (trio staffé, baseline signée), pas un gate de valeur. La première preuve de *valeur* arrive au Gate 1, mois 12, une fois **$11.45m bruts** (Y0+Y1) dépensés. | Les slides 2 et 18 insistent sur $2.90m. La slide 15 montre un creux de −$9.8m. | Le dire nous-mêmes : « $2.90m est l'engagement d'aujourd'hui ; le capital réellement à risque avant preuve de valeur est le creux : −$9.8m en base, −$11.5m en downside. » Y1 est débloqué cas par cas, et seulement 2.80 de Y1 est du capex. |
| 2 | **Le downside est doux.** 80–90 % des bénéfices, coûts +5–10 %, cash encore positif (+$2.27m), IRR +5.7 %. Le cours exige un downside à IRR négatif. | La propre slide du prof : « le pire cas doit être une vraie défaillance ». | Le workbook contient un **stress sévère** (bénéfices à 65 %, coûts +20 %, ramp-ups retardés, P12 non arrêté) : NPV **−$10.0m**, cash cumulé **−$9.0m** à Y5, creux **−$15.5m** *[recalculé depuis la feuille]*. Le citer, puis dire que les gates coupent la dépense avant d'y arriver. |
| 3 | **Le coût de l'inaction est petit et assumé.** $1.32m sur $6.94m de valeur de décision (19 %), trois expositions seulement. Un retard coûte $0.65m. | Exemple du cours : inaction −€16.7m contre ENPV +€3.7m. | Le défendre comme volontairement prudent, et montrer que la décision n'en dépend pas (§1). Ne pas le gonfler en direct. |
| 4 | **Le half budget a un IRR *supérieur* (34.8 % contre 27.8 %).** « Alors donnez-moi la moitié. » | La slide 26 leur offre l'argument. | Moitié = NPV attendue +$3.35m contre +$5.62m ; les six autres cas apportent +$2.27m. Et le Gate 0 rend déjà les cas complémentaires conditionnels à des baselines signées (§4). |
| 5 | **Le goulot repose sur une seule observation d'initié** (une branche). Toute la demande d'operating model (le trio) en dépend, et aucune ligne de bénéfice ne valorise le trio. | Audit Opus précédent : « une personne, un an, une filiale ». | C'est une hypothèse avec un test à 90 jours et un plan B (changer l'intervention si les données disent autre chose). Aucune NPV ne dépend du fait que le trio soit meilleur ; le downside porte déjà une adoption plus lente (§6). |

Coutures plus petites : le Gate 1 exige ≥3 cas avec bénéfice vérifié par la Finance au mois 12 alors que P03/P09/P12 ont 0 % de bénéfice en Y1 (§7) ; la consultation des représentants du personnel en France peut ne pas tenir en 90 jours ; la slide 14 dit « no scenario loses cash » (vrai pour le downside, faux pour le stress sévère : dire « no *modelled downside* »).

---

## 1. Coût de l'inaction trop faible

**Version orale (20 s) :** « Nous avons choisi de ne pas le gonfler. Nous ne comptons que la détérioration que nos projets peuvent réellement absorber : $1.32m de valeur actuelle, trois expositions nommées. Et la décision n'en a pas besoin : les projets seuls valent +$5.62m. Si vous pensez que l'inaction coûte plus cher, le dossier devient plus fort, pas plus faible. »

**Arguments de soutien (en utiliser deux, pas tous) :**
1. **Le contrefactuel n'est pas « pas d'IA ».** TotalEnergies fait déjà tourner plus de 10 000 modèles, ~100 solutions Digital Factory, et vient de s'engager à plus de €100m avec Mistral (15 sept. 2026). Notre programme est la correction du dernier kilomètre par-dessus. La perte à ne pas agir est donc une *accélération perdue*, petite par construction.
2. **Le secteur.** Hydrocarbures et raffinage sont des activités preneuses de prix, adossées à des actifs (11.2 Gboe de réserves, >12 ans ; coût de production $5.0/boe ; ROACE 12.6 % ; gearing 9.1 % au 30 sept. 2026). L'IA change la courbe de coûts, pas la structure de marché : aucun entrant « AI-native » ne prend des parts à une raffinerie ou à un champ en eaux profondes. Les pairs ont les mêmes outils, donc la pression porte sur la marge et le coût, ce que mesurent nos trois expositions.
3. **Le coût du retard est faible parce que les bénéfices sont décalés, pas perdus** ($0.65m = 9 % de la NPV de base). C'est aussi pourquoi la logique d'option fonctionne : la Tranche 1 est de $2.90m, nous achetons de l'information à bas prix au lieu de brûler une plateforme.
4. **Nous refusons l'érosion inventée.** Une version antérieure portait un pool clients de $150m et 50 % d'évitement ; les revues n'ont trouvé ni pool qualifiant ni chaîne causale, donc il a été retiré (`work/research/overlap_and_inaction_review.md`). Le rapport dit aussi que les annonces des pairs (Equinor $120m cumulés en maintenance prédictive, BP en planification de puits) ne prouvent pas un écart pour TotalEnergies.
5. **Les talents** sont une exposition réelle mais non chiffrée (l'URD p. 318 cite la concurrence sur les compétences). Nous la suivons comme indicateur avancé, pas comme montant de cash.

**À ne pas dire :** « les concurrents vont nous prendre des parts de marché » (aucune preuve), « l'IA est existentielle pour TotalEnergies ».

**Question piège : « Si l'inaction est si peu chère, pourquoi maintenant ? »** → « C'est une option sans regret, par étapes, pas une plateforme en feu. Les plateformes (AspenTech, Cognite) se déploient jusqu'en 2027–28 et la Digital Line a été créée en sept. 2025 ; la fenêtre pour installer la livraison, c'est maintenant, et la première tranche représente 0.01 % du cash-flow opérationnel annuel ($27.8bn en FY2025). »

---

## 2. Écart entre le downside (−$1.30m) et la base (+$7.11m) ; optimisme des rendements

**Version orale :** « Les $8.4m d'écart viennent presque entièrement du calendrier et de la taille des bénéfices. La valeur actuelle des bénéfices passe de $29.9m à $20.0m ; les coûts augmentent de moins de $1m. Nous l'affichons, nous ne le cachons pas. Notre marge de sécurité : le portefeuille atteint l'équilibre si les bénéfices sont 30 % sous la base. »

**Décomposition** *[recalculé]* : valeur actuelle à 10 %, base → downside : bénéfices 29.9 → 20.0 (−9.9) ; coûts 18.2 → 18.9 (+0.8) ; impôt 4.6 → 2.4 (+2.2 de coussin). Net −8.4. Environ 85 % de l'écart vient des bénéfices (ramp-up, facteur 80–90 %, recettes P12 supprimées).

**Pourquoi les rendements paraissent élevés, honnêtement :**
- L'IRR porte sur une **base petite et légère en capital** : capex de seulement $5.69m (26 % de l'enveloppe) ; le reste est de l'opex, passé en charge et déductible. Les plateformes sont réutilisées (AspenTech, Cognite) : nous payons l'intégration marginale, pas la plateforme.
- **Pas de valeur terminale** ; le bénéfice en régime de croisière en Y5 est de $13.5m/an pour $2.8m de coûts récurrents (4.8×), mais les années 6+ ne comptent pour rien.
- Chaque bénéfice est un **petit pourcentage** d'une très grande base (0.45 % de débit, 4 % de gaspillage × 25 %, 2 % de carburant). Facile à croire, difficile à vérifier, d'où les gates avec vérification Finance.
- **Pas dépendant de H3 :** la NPV hors P12 est de +$6.93m ; hors P03 +$5.14m ; hors P12, P03 et P13 +$4.45m *[recalculé]*. Les recettes P12 ($4.4m, non contractualisées) n'ajoutent que +$0.18m de NPV.

**Table de sensibilité** *[recalculé, cas de base, NPV à 10 %]* :

| Choc | NPV $m |
|---|---:|
| Base | +7.11 |
| Bénéfices −20 % | +2.55 |
| Bénéfices −30 % | +0.25 (équilibre ≈ −30 %) |
| Bénéfices −40 % | −2.06 |
| Bénéfices −50 % | −4.39 |
| Coûts +20 % | +4.39 |
| Coûts +50 % | +0.30 (équilibre ≈ +50 %) |
| Coûts +100 % | −6.52 |

**Robustesse de l'espérance** *[recalculé]* : poids 50/30/20 → +$3.94m ; 60/30/10 → +$2.58m. En remplaçant le downside par le stress sévère à 30 % → **+$3.0m** ; à 50 % de stress sévère → −$0.4m. L'espérance reste donc positive sauf si le cas sévère est plus probable qu'improbable.

**À admettre si on insiste :** les poids 30/50/20 sont des jugements ; toutes les hypothèses de bénéfices sont des hypothèses ; des dépassements de +5–10 % sont doux (Flyvbjerg et Budzier ont trouvé 27 % de dépassement moyen sur 1 471 projets IT, et environ 1 sur 6 dans la queue extrême proche de +200 % ; [arXiv:1304.0265](https://arxiv.org/abs/1304.0265)). Notre réponse est le seuil d'équilibre à +50 % et les gates qui coupent la dépense, pas l'affirmation que les dépassements n'arriveront pas. Les risques des projets sont **corrélés** (un seul goulot d'adoption) : le downside se lit comme un événement joint, non diversifié.

**Question tueuse (issue de notre propre audit) : « Si c'est si facile, pourquoi mes équipes ne l'ont-elles pas déjà fait ? »**
→ « Parce que la contrainte n'est pas la technologie. Temps gagné n'est pas cash gagné : les jours de rig ne comptent que si le contrat baisse le paiement (P03), une prédiction ne compte que si un baril est vendu (P01), les démarques ne comptent que si elles sont incrémentales (P13). Nous finançons l'organisation qui transforme des solutions en cash mesuré, et chaque cas nomme son hypothèse la plus faible et son seuil d'équilibre. »

---

## 3. « Vos projets sont surtout de l'opex, pas du capex » : s'en servir, mais connaître l'autre tranchant

**Pour nous :** peu de capital à risque ($5.69m de capex, Y0–Y1 seulement), peu d'actifs échoués si on s'arrête, coûts réversibles et pouvant être suspendus à chaque gate ; 40 % puis 60 % du coût récurrent passent aux branches.
**Contre nous (à anticiper) :** le récurrent représente **55 % de l'enveloppe ($12.12m)** ; dès Y4 c'est un coût permanent de $2.7–2.8m/an ; « s'arrêter » ne récupère pas le déjà dépensé. Réponse : le Gate 2 exige des bénéfices annuels vérifiés ≥ coûts récurrents et 60 % de cofinancement des branches ; les projets qu'une branche ne cofinance pas ne continuent pas.
Aussi : un modèle opex-lourd signifie que les économies peuvent être absorbées par le coût courant de l'outil lui-même, c'est pourquoi chaque cas compte le cash incrémental net, après coûts récurrents et impôt.

---

## 4. « Pourquoi ce budget et pas la moitié ? »

**Version orale :** « La moitié est notre plan de repli et le Gate 0 nous y amène naturellement. Les cas complémentaires (P02, P04, P05, P08, P09) ne sont débloqués qu'après une baseline signée par la Finance. Mais la moitié abandonne $2.3m de NPV attendue et supprime E01, le registre de modèles que le calendrier de l'AI Act (dispositions haut risque applicables dès le 2 déc. 2027) rend nécessaire. »

Chiffres : les quatre cas phares coûtent $11.35m (51.7 %) ; IRR de base 34.8 %, downside 6.4 %, NPV attendue +$3.35m contre +$5.62m pour le plein ; cas complémentaires individuellement : P04 +$1.05m, P08 +$0.99m, P02 +$0.99m, P05 +$0.42m, P09 +$0.21m ; E01 −$0.76m (c'est un coût, le bénéfice est dans les autres cas).
**Point faible honnête :** l'IRR plus élevé de la moitié est un fait d'efficacité du capital ; nous choisissons la NPV absolue et l'étendue. De plus, la moitié exclut E01 et « s'appuie sur les contrôles existants ».
**À ne pas dire :** « la moitié détruit la cohérence stratégique » (le script du cours) ; nos propres chiffres montrent que la moitié fonctionne encore. Dire : « la moitié est viable, et c'est ce que produirait un Gate 0 raté ».

---

## 5. Secteur, « déjà sur de bons rails », « pourquoi est-ce à mon agenda ? »

- Vérification d'échelle : programme de $21.94m sur 6 ans contre un CFFO FY2025 de $27.8bn et des investissements nets de $17.1bn : ~0.1 %. Ce n'est pas un pari stratégique ; c'est une preuve du modèle de livraison. Mistral seul dépasse €100m.
- Position : stratégie, données et expérience de livraison obtiennent 3–3.5 dans notre évaluation de maturité « outside-in » ; organisation et gouvernance 2.5. Nous ne disons pas que le groupe est en retard ; nous disons que la valeur est freinée par *l'organisation du travail projet*.
- Discipline de capital : capex réduit de $1bn/an, plan d'économies de $12.5bn 2026–2030, distribution >40 % du cash-flow. Nous nous insérons : petit, par étapes, cofinancé par les branches.
- **Ne pas prétendre que l'IA contribue au plan de $12.5bn** : ses leviers ne sont pas publiés (question ouverte Q06). Si on demande « est-ce déjà dans mon plan d'économies ? » : « Les baselines signées par la Finance excluent les économies déjà planifiées ; seul le cash incrémental compte. Nous ne pouvons pas vérifier le recouvrement avec des données publiques, c'est précisément ce que contrôle le Gate 0. »
- Risque inverse : « pas disrupté » appelle « alors ne dépensez pas ». Toujours associer à « sans regret, par étapes ».

---

## 6. Goulot d'étranglement et trio

- Preuves : publiques (URD p. 138, risque lié au rythme d'adaptation organisationnelle et des compétences ; Digital Line créée en sept. 2025) plus une observation locale (CLM-074). **Dire « hypothèse » et « l'observation de notre initié dans une branche ».**
- C'est testé, pas présumé : délai avant première mise en service, intervalle entre revues, projets par responsable, utilisateurs actifs. Si l'accès aux données ou un contrat est la vraie contrainte, nous changeons l'intervention.
- Le coût est dans les enveloppes projets (talents et conduite du changement : $4.07m sur $16.40m en Y0–Y3). Pas de nouvelle organisation, pas de nouvelle plateforme.
- Q : « Qu'apporte le trio par rapport à aujourd'hui ? » → « Nous ne comptons pas de bénéfice séparé ; les rendements des projets sont autonomes et le downside suppose déjà une adoption plus lente. Le trio est le moyen d'obtenir les ramp-ups du cas de base ; la baseline à 90 jours des délais actuels est notre contrôle. »
- Le frottement de la double hiérarchie est nommé comme risque avec une escalade (sponsor sous une semaine).

---

## 7. Gates et règles d'arrêt

- **Format d'une règle d'arrêt (question 2 du cours) :** métrique + seuil + date + responsable + action. Utiliser la slide 20 : p. ex. <40 % d'utilisateurs éligibles actifs au mois 6 → remédier ou arrêter sous 30 jours (sponsor de branche + CHRO) ; <60 % de décisions dans l'outil au mois 12 → pas d'extension ; pas de bénéfice vérifié par la Finance ou NPV prospective négative au mois 12 → pause/redesign/arrêt (CFO + sponsor) ; contrat P03 ne permettant pas la capture au Gate 0 → arrêt de ce périmètre ; P12 sans clearance IP ni deux développeurs d'ici Y2 → arrêt, $0.10m de clôture.
- **Point faible :** le Gate 1 exige ≥3 cas avec bénéfice incrémental vérifié par la Finance au mois 12, alors que les ramp-ups de base sont de 0 % (P03, P09, P12) ou 20 % (P01, P04, P08) en Y1. Réponse : les trois candidats sont P13 (ramp-up de 50 % en Y1), P01 et P05 (20–25 %), mesurés contre des baselines préenregistrées sur des cohortes pilotes ; s'il y en a moins de trois, le Gate 1 met en pause les cas défaillants, ce qui est la conception annoncée.
- **Point faible :** le Gate 0 à J+90 inclut la consultation des salariés ; en France elle peut être plus longue. Réponse : la consultation démarre dans les 90 premiers jours ; un cas qui n'est pas prêt n'est tout simplement pas débloqué, son enveloppe est gardée.
- Pire cas avec gates : si tout échoue au mois 12, la sortie de cash est Y0+Y1 ≈ $11–13.7m brut en creux (−$11.5m downside ; −$13.7m sévère) *[recalculé]* ; Y2 et après ne sont pas débloqués.

---

## 8. Attaques au niveau des cas

**P01 raffinage.** Hypothèses : 250 kb/j sur deux sites, 0.45 % récupéré, 70 % vendu, $6/bbl, $0.15m de réparations. NPV nulle à 57.6 % du bénéfice. Si « $6/bbl est bas » : le marqueur ERM du T3 2026 était de $33.2/b (un marqueur de marché, pas notre marge réalisée), donc $6 est prudent, mais cyclique. Référence externe : les chiffres publiés de maintenance prédictive (20–30 % de coût de maintenance, 10–20 % d'arrêts) viennent surtout d'éditeurs ou d'attributions floues ; McKinsey note des prérequis (historique de données, capteurs, forte valeur de l'arrêt). À traiter comme contexte, jamais comme preuve. Les $120m d'Equinor sont cumulés depuis 2020, partenaires inclus. « Pourquoi pas déjà fait ? » → la plateforme AspenTech ne se déploie que jusqu'en 2027–28.

**P03 forage.** Hypothèse la plus faible : le contrat. 80 % de part économique × 75 % d'évitabilité du paiement. À 40 % de part, le bénéfice est divisé par deux à $1.44m, sous le seuil de $1.66m ; d'où le test de contrat du Gate 0 avant toute dépense Y1. Mero est opéré par Petrobras (TotalEnergies 19.3 %), donc nous ne supposons pas de déploiement unilatéral : le périmètre est « rigs opérés ». 6 jours évitables par rig et par an est une petite tranche.

**P13 retail.** €1.0m pour 100 stations (calibration de l'initié). Sans les démarques (€0.25m), le bénéfice de €0.385m < seuil de €0.446m. Mitigation : démarques mesurées d'abord sur des cohortes SKU séparées ; repli prévision seule ; les étiquettes doivent battre la prévision seule.

**P12 e-SAF.** H3 sans délai de retour inventé ; les recettes conditionnelles de $0.60m/$1.50m/$2.30m en Y3–Y5 ne sont pas contractualisées ; contribution à la NPV de base +$0.18m ; le downside s'arrête en Y2 avec $0.10m de clôture. « Pourquoi H3 seulement à 10 % ? » → option bornée, Mistral finance déjà le sous-sol donc nous évitons le doublon.

**Mix d'horizons 70/20/10.** Inclinaison délibérée vers H1 pour des actifs industriels à cycle long (« deviate on purpose » du cours) : 70.5/19.4/10.2 sur l'investissement ponctuel, 65.6/21.4/13.0 sur la dépense totale.

**Taux d'actualisation.** 10 % = 7.0 % de WACC post-impôt publié pour les tests de dépréciation (FY2025) + 3 points de prime IA ; hurdles par projet de 9–12 %. La prime est notre hypothèse. La sensibilité de ±1 point de WACC est dans la note de politique. L'IRR des flux attendus (27.8 %) n'est pas un IRR attendu.

---

## 9. Fiche de chiffres (une page)

| Élément | Valeur |
|---|---|
| Demande aujourd'hui | $2.90m Tranche 1 ; enveloppe $21.94m plafond ; ponctuel $9.82m (capex $5.69m) ; récurrent $12.12m |
| Gates | Jour 90 → $8.55m ; mois 12 → $2.31m ; mois 24 → run Y3–Y5 |
| NPV / IRR attendus | +$5.62m / 27.8 % (30/50/20) |
| NPV base / downside / upside | +7.11 / −1.30 / +12.28 ; IRR 32.6 % / 5.7 % / 48.2 % |
| Cash à Y5 | +13.78 / +2.27 / +20.83 ; attendu +11.74 |
| Creux (fin Y1) | −9.8 base, −10.2 attendu, −11.5 downside ; stress sévère −15.5 |
| Point d'équilibre | 3.3 ans base, 3.4 ans attendu, ~4.6 ans downside |
| Stress sévère | NPV −$10.0m, cash −$9.0m à Y5 |
| Inaction | +$1.32m (P01 0.51, P03 0.54, P08 0.27) ; valeur de décision $6.94m ; retard d'un an −$0.65m |
| Half budget | $11.35m, IRR 34.8 % / 6.4 %, NPV attendue +$3.35m |
| Chocs d'équilibre | bénéfices −30 % ; coûts +50 % |
| Cofinancement | branches 40 % en Y2, 60 % en Y3–Y5 |
| Contexte groupe | CFFO FY2025 $27.8bn ; investissements nets $17.1bn ; ROACE 12.6 % ; gearing 9.1 % (30 sept. 2026) ; programme Mistral >€100m |

## 10. Actions suggérées avant la session

1. Décider qui répond à quoi : Yoni (rendements, inaction, half budget), Vincent (portefeuille, cas), Alexandre (goulot), Nahel (gates, règles d'arrêt).
2. Ne rien ajouter au deck à ce stade. Si une seule modification est permise : texte de la slide 14 « no scenario loses cash » → « the downside still returns its cash » ; et la formulation « at risk » de la slide 2 → « committed ».
3. Garder les slides 14, 20, 21, 22, 26 à un clic pour le Q&A.
4. Répéter les trois questions du cours (pire cas, ce qui l'arrête, si on ne fait rien) avec les chiffres exacts ci-dessus.

**Sources externes utilisées :** Flyvbjerg et Budzier, « Why Your IT Project May Be Riskier than You Think » ([arXiv:1304.0265](https://arxiv.org/abs/1304.0265)) ; McKinsey, [A smarter way to digitize maintenance and reliability](https://www.mckinsey.com/capabilities/operations/our-insights/a-smarter-way-to-digitize-maintenance-and-reliability) (prérequis uniquement ; chiffres cités de seconde main ailleurs) ; communiqué TotalEnergies–Mistral du 15 sept. 2026 (dans `sources/primary/`). Une recherche web n'a trouvé aucune cible publiée de valeur IA chez TotalEnergies, ce qui justifie de ne pas en revendiquer une.
