import flet as ft
import random
import requests
from selectorlib import Extractor


def main(page: ft.Page):
    categories = {
			"Cereales" : ['cereale', 'blé ', 'riz ', 'mil '],
			"Fruits": ['fruit', 'ananas', 'mangue', 'pasteque', 'noix', 'coco', 'cacao', 'café'],
			"Legumes": ['legume', 'carotte', 'tomate', 'tasba', 'ndole', 'granuleux', 'arachide', 'haricot', 'soja', 'poids de terre'],
			"Tubercules": ['tubercule', 'manioc', 'patate', 'igname', 'macabo', 'taro'],
			"Toutes categorie": [' ']
			}

    r1 = requests.get('https://www.afrique-agriculture.org/')
    e1 = Extractor.from_yaml_string("""
posts:
    css: 'article.node article.node'
    xpath: null
    multiple: true
    type: Text
    children:
        title:
            css: a.node-url
            xpath: null
            type: Text
        comment:
            css: p.chapo
            xpath: null
            type: Text
        image:
            css: img
            xpath: null
            type: Image
        url:
            css: a.node-url
            xpath: null
            type: Link
    """)
    actu1 = e1.extract(r1.text)

    r2 = requests.get('https://afrique.latribune.fr/entreprises/agriculture')
    e2 = Extractor.from_yaml_string("""
posts:
    css: article.article-wrapper
    xpath: null
    multiple: true
    type: Text
    children:
        title:
            css: 'h2 a'
            xpath: null
            type: Text
        comment:
            css: p
            xpath: null
            type: Text
        image:
            css: img
            xpath: null
            type: Image
        url:
            css: 'h2 a'
            xpath: null
            type: Link
    """)
    actu2 = e2.extract(r2.text)

    r3 = requests.get('https://www.scidev.net/afrique-sub-saharienne/agriculture/')
    e3 = Extractor.from_yaml_string("""
posts:
    css: div.article-list
    xpath: null
    multiple: true
    type: Text
    children:
        title:
            css: strong
            xpath: null
            type: Text
        comment:
            css: 'h3 a'
            xpath: null
            type: Text
        image:
            css: img.lazyloaded
            xpath: null
            type: Image
        url:
            css: 'h3 a'
            xpath: null
            type: Link
    """)
    actu3 = e3.extract(r3.text)
    
    #actu1 = {'posts': [{'title': 'Au Kenya, la promesse agricole de Shamba Pride séduit les investisseurs', 'comment': "C'est un tour de table de 3,7 millions de dollars que vient de finaliser la startup kenyane, riz désireuse de...", 'image': 'https://static.latribune.fr/homepage_river/2307512/shamba-pride.jpg', 'url': 'https://afrique.latribune.fr/africa-tech/startups/2024-01-23/au-kenya-la-promesse-agricole-de-shamba-pride-seduit-les-investisseurs-988582.html'}, {'title': 'Maroc\xa0: OCP Group finalise lacquisition de sa participation de 50% dans le capital de la s...', 'comment': 'Avec cette acquisition par le géant marocain des phosphates, la capacité de production de GlobalFeed, une...', 'image': 'https://static.latribune.fr/homepage_river/2171581/globalfeed-espagne.jpg', 'url': 'https://afrique.latribune.fr/afrique-du-nord/maroc/2023-05-20/maroc-ocp-group-finalise-l-acquisition-de-sa-participation-de-50-dans-le-capital-de-la-societe-espagnole-globalfeed-963072.html'}, {'title': '«\xa0Nous ambitionnons de  produire un million de tonnes dammoniac vert dici 2027 » (Karim...', 'comment': "A l'occasion des Tables rondes de l'Arbois, Karim Saoud, vice-président\xa0of Water and Energy du groupe mar...", 'image': 'https://static.latribune.fr/homepage_river/2170005/karim-saoud-ocp-group.jpg', 'url': 'https://afrique.latribune.fr/think-tank/entretiens/2023-05-19/nous-ambitionnons-de-produire-un-million-de-tonnes-d-ammoniac-vert-d-ici-2027-karim-saoud-ocp-group-962815.html'}, {'title': 'Angola\xa0: Deutsche Bank finance la future plus grande usine de broyage de soja et de tournes...', 'comment': "Située à Lobito, l'usine entièrement automatisée aura une capacité de traitement pouvant atteindre 4 000...", 'image': 'https://static.latribune.fr/homepage_river/2149860/usine-broyage-soja-angola.jpg', 'url': 'https://afrique.latribune.fr/finances/investissement/2023-04-12/angola-deutsche-bank-finance-la-future-plus-grande-usine-de-broyage-de-soja-et-de-tournesol-en-afrique-958543.html'}, {'title': 'Afrique-France\xa0: ALFA, le nouvel outil de diplomatie économique pour la coopération agricol...', 'comment': "L'association ALFA a été officiellement constituée lors d'une assemblée générale de ses membres fondateur...", 'image': 'https://static.latribune.fr/homepage_river/2143161/ait-taleb-advens-geocoton.jpg', 'url': 'https://afrique.latribune.fr/economie/strategies/2023-03-31/afrique-france-alfa-le-nouvel-outil-de-diplomatie-economique-pour-la-cooperation-agricole-passe-a-la-vitesse-superieure-957357.html'}]}
    
    #actu2 = {'posts': [{'title': 'Le Maroc et le Libéria unissent leurs forces pour la durabilité des ressources marines', 'comment': 'Le 26 janvier dernier, conformément aux Hautes Orientations de Sa Majesté Le Roi Que Dieu Lassiste, le ministre de lAgriculture, de la Pêche Maritime, du Développement Rural et des Eaux et Forêts, M. Mohammed Sadiki sest rendu au Libéria, sur invitation des Autorités du Libéria. Lobjectif de...', 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/dsc_0172.jpg?itok=OyUJu6au', 'url': '/articles/lessentiel/le-maroc-et-le-liberia-unissent-leurs-forces-pour-la-durabilite-des-ressources'}, {'title': 'Booster la petite agriculture en misant sur le bio', 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/dossier_maroc_bio_photo_2_oleiculture-olives.jpg?itok=5_sYsUll', 'url': '/articles/filieres/booster-la-petite-agriculture-en-misant-sur-le-bio'}, {'title': 'La poule pantalonnée, une alternative bio au poulet de chair', 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/des_coq_brahma_de_la_ferme_de_bilone_photo_viviane.jpg?itok=aI1XbaSb', 'url': '/articles/filieres/la-poule-pantalonnee-une-alternative-bio-au-poulet-de-chair'}, {'title': 'La Guinée engagée dans le combat contre la grippe aviaire', 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/des_poulets_pour_lelevage_dans_une_ferme_a_conakry_photo_nantady_camara.jpg?itok=dHMiqOHj', 'url': '/articles/lessentiel/la-guinee-engagee-dans-le-combat-contre-la-grippe-aviaire'}, {'title': 'Quelles mesures de prévention de la boiterie chez les bovins ?', 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/photo_2_un_pied_de_bovin_souffrant_de_boiterie_credit_m.delacroix.jpeg?itok=bpV6Fnxp', 'url': '/articles/technique-animale/quelles-mesures-de-prevention-de-la-boiterie-chez-les-bovins'}, {'title': "Optimiser la gestion du bétail grâce aux technologies de l'information", 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/5f429d43d0d5f722249176_663063591.jpg?itok=N5vQgGqd', 'url': '/articles/lessentiel/optimiser-la-gestion-du-betail-grace-aux-technologies-de-linformation'}, {'title': 'Centre de formation professionnelle agricole de Thibar : une place de choix pour lélevage avicole', 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/article_tunisie_bassecour_pour_poulet_fermier.jpg?itok=1e_nqQM3', 'url': '/articles/lessentiel/centre-de-formation-professionnelle-agricole-de-thibar-une-place-de-choix-pour'}, {'title': 'La filière se porte mieux !', 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/article_cote_divoire_eleveur_ivoirien_de_poulet_de_chair-poulet_credit_programme_dappui_a_la_production_avicole_nationale850.jpg?itok=qLd_QwV5', 'url': '/articles/lessentiel/la-filiere-se-porte-mieux'}, {'title': 'La Cada mise sur une aviculture moderne et durable en Afrique', 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/youssef_alaoui_credit_fisa.jpg?itok=9IvMdVlw', 'url': '/articles/lessentiel/la-cada-mise-sur-une-aviculture-moderne-et-durable-en-afrique'}, {'title': '« La hausse des prix des aliments pour volaille est pratiquée par les importateurs »', 'comment': None, 'image': 'https://www.afrique-agriculture.org/sites/afrique_agriculture/files/styles/teaser/public/bandeau_site_arbo_9.png?itok=Z2xTFSLz', 'url': '/articles/lessentiel/la-hausse-des-prix-des-aliments-pour-volaille-est-pratiquee-par-les-importateurs'}]}
    
    #actu3 = {'posts': [{'title': 'Actualités', 'comment': 'La sécheresse frappe près dune personne sur quatre dans le monde', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/news/nearly-one-in-four-people-now-drought-stricken-un/'}, {'title': 'Contenu sponsorisé', 'comment': 'Recycler la fiente de poules pour réchauffer les poussinières', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/supported-content/recycler-la-fiente-de-poules-pour-rechauffer-les-poussinieres/'}, {'title': 'Actualités', 'comment': 'Une variété de riz sans danger pour les diabétiques', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/news/breakthrough-makes-rice-guilt-free-for-diabetics/'}, {'title': 'Actualités', 'comment': 'Lélevage bovin sous la menace du stress thermique', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/news/lelevage-bovin-sous-la-menace-du-stress-thermique/'}, {'title': 'Actualités', 'comment': 'Le sommet africain sur le climat ignore les petits exploitants', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/news/africa-climate-summit-pledges-ignore-smallholders/'}, {'title': 'Actualités', 'comment': 'Une technique pour maîtriser les ravageurs et booster les récoltes', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/news/push-pull-tech-increases-maize-yields/'}, {'title': 'Actualités', 'comment': 'Du riz résistant aux inondations pour les producteurs africains', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/news/du-riz-resistant-aux-inondations-pour-les-producteurs-africains/'}, {'title': 'Actualités', 'comment': 'Le Sénégal produit 8 types de blé adaptés à la chaleur', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/news/le-senegal-produit-8-types-de-ble-adaptes-a-la-chaleur/'}, {'title': 'SciDev.Net sur le terrain', 'comment': 'La diversité, solution à linsécurité alimentaire en Afrique', 'image': None, 'url': 'https://www.scidev.net/afrique-sub-saharienne/scidev-net-at-large/la-diversite-solution-a-linsecurite-alimentaire-en-afrique/'}]}

    background_color = "#f2f2f2"
    title_color = "black"
 
    categorized_actu = {}
    all_cat = []

    for category, elements in categories.items():
        liste = []
        for elt in elements:
            for post in actu1["posts"]:
                if post['comment'] != None and (elt.lower() in post['title'].lower() or elt.lower() in post['comment'].lower()):
                    liste.append(post)
            for post in actu2["posts"]:
                if post['comment'] != None and (elt.lower() in post['title'].lower() or elt.lower() in post['comment'].lower()):
                    liste.append(post)
            for post in actu3["posts"]:
                if post['comment'] != None and (elt.lower() in post['title'].lower() or elt.lower() in post['comment'].lower()):
                    liste.append(post)
                    
            all_cat.append(liste)
        categorized_actu[category] = liste
        
    categories['Toutes categorie'] = all_cat
   
    
    image_acceuil = ft.Row(
      width = 360,
      height = 146,
    	scroll = "auto"
    )
    for i in range(1, 4):
    	image_acceuil.controls.append(
    		ft.Container(
    			bgcolor = "#c5c5c5",
    			height = 125,
    			width = 220,
    			border_radius = 13,
				content = ft.Column(
					controls = [
						ft.Image(
							src=f"img/img"+ str(i) +".png",
        					fit=ft.ImageFit.CONTAIN,
						)
					]
				)
    		)
    	)
    	
    
    categ = list(categories.keys())
    liste_categories = ft.Column(
    	height = 290,
    	scroll= ft.ScrollMode.ALWAYS,
		controls = [
    		ft.Container(
    			width = 360,
    			height = 90,
    			bgcolor = "#c4c4c4",
    			border_radius = 15,
    			padding = ft.padding.only(left = 20, top = 10),
    			on_click=lambda _: page.go("/store"),
    			
    			content = ft.Row(
					controls = [
						ft.Column(
							controls = [
								ft.Text(value = categ[0], size = 20, color = "black", weight = "bold"),
								ft.Text(value = "News de : {}".format(categ[0]), color = "#181818"),
								ft.Container(
									width = 200,
									height = 7,
									bgcolor = "white",
									border_radius = 20,
									padding = ft.padding.only(right = random.randint(3, 6) * 30),
									content = ft.Container(
										bgcolor = "#c0e0de"
									)
								),
							]
						),
						ft.ElevatedButton(text = "Select", on_click=lambda _: page.client_storage.set("category", categ[0])),
						ft.Image(
							src=f"img/"+ categ[0] +".png",
							width=70,
							fit=ft.ImageFit.CONTAIN,
						)
      
					]
				)
    		),
    	
			ft.Container(
    			width = 360,
    			height = 90,
    			bgcolor = "#c4c4c4",
    			border_radius = 15,
    			padding = ft.padding.only(left = 20, top = 10),
    			on_click=lambda _: page.go("/store"),
    			
    			content = ft.Row(
					controls = [
						ft.Column(
							controls = [
								ft.Text(value = categ[1], size = 20, color = "black", weight = "bold"),
								ft.Text(value = "News de : {}".format(categ[1]), color = "#181818"),
								ft.Container(
									width = 200,
									height = 7,
									bgcolor = "white",
									border_radius = 20,
									padding = ft.padding.only(right = random.randint(3, 6) * 30),
									content = ft.Container(
										bgcolor = "#c0e0de"
									)
								),
							]
						),
						ft.ElevatedButton(text = "Select", on_click=lambda _: page.client_storage.set("category", categ[1])),
						ft.Image(
							src=f"img/"+ categ[1] +".png",
							width=70,
							fit=ft.ImageFit.CONTAIN,
						)
      
					]
				)
    		),
    	
			ft.Container(
    			width = 360,
    			height = 90,
    			bgcolor = "#c4c4c4",
    			border_radius = 15,
    			padding = ft.padding.only(left = 20, top = 10),
    			on_click=lambda _: page.go("/store"),
    			
    			content = ft.Row(
					controls = [
						ft.Column(
							controls = [
								ft.Text(value = categ[2], size = 20, color = "black", weight = "bold"),
								ft.Text(value = "News de : {}".format(categ[2]), color = "#181818"),
								ft.Container(
									width = 200,
									height = 7,
									bgcolor = "white",
									border_radius = 20,
									padding = ft.padding.only(right = random.randint(3, 6) * 30),
									content = ft.Container(
										bgcolor = "#c0e0de"
									)
								),
							]
						),
						ft.ElevatedButton(text = "Select", on_click=lambda _: page.client_storage.set("category", categ[2])),
						ft.Image(
							src=f"img/"+ categ[2] +".png",
							width=70,
							fit=ft.ImageFit.CONTAIN,
						)
      
					]
				)
    		),
    	
			ft.Container(
    			width = 360,
    			height = 90,
    			bgcolor = "#c4c4c4",
    			border_radius = 15,
    			padding = ft.padding.only(left = 20, top = 10),
    			on_click=lambda _: page.go("/store"),
    			
    			content = ft.Row(
					controls = [
						ft.Column(
							controls = [
								ft.Text(value = categ[3], size = 20, color = "black", weight = "bold"),
								ft.Text(value = "News de : {}".format(categ[3]), color = "#181818"),
								ft.Container(
									width = 200,
									height = 7,
									bgcolor = "white",
									border_radius = 20,
									padding = ft.padding.only(right = random.randint(3, 6) * 30),
									content = ft.Container(
										bgcolor = "#c0e0de"
									)
								),
							]
						),
						ft.ElevatedButton(text = "Select", on_click=lambda _: page.client_storage.set("category", categ[3])),
						ft.Image(
							src=f"img/"+ categ[3] +".png",
							width=70,
							fit=ft.ImageFit.CONTAIN,
						)
      
					]
				)
    		),
    	
			ft.Container(
    			width = 360,
    			height = 90,
    			bgcolor = "#c4c4c4",
    			border_radius = 15,
    			padding = ft.padding.only(left = 20, top = 10),
    			on_click=lambda _: page.go("/store"),
    			
    			content = ft.Row(
					controls = [
						ft.Column(
							controls = [
								ft.Text(value = categ[4], size = 20, color = "black", weight = "bold"),
								ft.Text(value = "News de : {}".format(categ[4]), color = "#181818"),
								ft.Container(
									width = 200,
									height = 7,
									bgcolor = "white",
									border_radius = 20,
									padding = ft.padding.only(right = random.randint(3, 6) * 30),
									content = ft.Container(
										bgcolor = "#c0e0de"
									)
								),
							]
						),
						ft.ElevatedButton(text = "Select", on_click=lambda _: page.client_storage.set("category", categ[4])),
						ft.Image(
							src=f"img/"+ categ[4] +".png",
							width=70,
							fit=ft.ImageFit.CONTAIN,
						)
      
					]
				)
    		),
    	
      ],
    )
    
    #category = 'Toutes categorie'
    #print(page.client_storage.get("category"))
    #category = 'Toutes categorie' if page.client_storage.get("category") == None else page.client_storage.get("category")
    def set_categ(route):
        global category
        category = page.client_storage.get("category")
        page.client_storage.clear()
        
    
    news = ft.Column(
			scroll= ft.ScrollMode.ALWAYS,
    )
    for elt in categorized_actu[category]:
        img_src = "https://www.shutterstock.com/image-vector/stop-icon-no-sign-symbol-260nw-492169339.jpg" if elt['image'] == None else elt['image']
    	
        news.controls.append(
    		ft.Container(
    			width = 360,
    			height = 380,
    			bgcolor = "#c4c4c4",
    			border_radius = 10,
    			padding = ft.padding.only(left = 15, top = 10, bottom = 10, right = 15),
    			
    			content = ft.Column(
    				controls = [
    					ft.Container(
							bgcolor = "#f1f1f1f1",
							height = 145,
							width = 320,
							border_radius = 13,
							content = ft.Column(
								controls = [
									ft.Image(
										src = img_src,
										width = 320,
										fit=ft.ImageFit.CONTAIN,
									)
								]
							)

						),
		    			ft.Text(value = elt['title'], size = 15, color = "black", weight = "bold"),
		    			ft.Text(value = elt['comment'], color = "#181818"),
		    			ft.Container(
		    				width = 320,
		    				height = 7,
		    				bgcolor = "white",
		    				border_radius = 20,
		    				padding = ft.padding.only(right = random.randint(3, 6) * 30),
		    				content = ft.Container(
		    					bgcolor = "#c0e0de"
		    				)
		    			),
						ft.ElevatedButton("Lire la suite", on_click=lambda _: page.go(elt['url'])), #-----------------------
						
    				]
    			)
    		),
    	)
    
    contenu_page1 = ft.Container(
		width = 360,
		border_radius = 30,
  		padding = ft.padding.only(left = 15, right = 15),
		content = ft.Column(
			controls = [
				ft.Container(height = 5),
				ft.Row(
					alignment = 'spaceBetween',
					controls = [
						ft.Container(
							content = ft.Icon(ft.icons.MENU, color = title_color)
						),
						
							ft.Row(
								controls = [
									ft.Text(value = "AGRI-VEILLE", size = 30, color = title_color, weight = 'bold')
								]
							),
						
						ft.Row(
							controls = [
								ft.Icon(ft.icons.SEARCH, color = title_color),
								ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED, color = title_color),
							]
						)
					]
				),
				
				ft.Container(height = 10),
				
				ft.Text(value = "Du nouveau en Agriculture??", color = title_color, size = 20),
				
				ft.Container(
					content = image_acceuil
				),
				
				#-----------------
				
				ft.Container(height = 20),
				
				ft.Text("CATEGORIES", size = 25, color = title_color),
				
				ft.Container(
					bgcolor = background_color,
					content = liste_categories,
					
				)
				
			]
		)
	)
    
    background_page1 = ft.Container(
		width = 360,
		height = 660,
		bgcolor = background_color,
		border_radius = 30,
		content = ft.Column(
			controls = [
					ft.Stack(
						controls = [
							contenu_page1
						]
					)
				]
      )
	)
    
    contenu_page2 = ft.Container(
		width = 360,
		border_radius = 30,
		padding = ft.padding.only(left = 15, right = 15),
		content = ft.Column(
			controls = [
				
				ft.Container(height = 5),
				ft.Row(
					alignment = 'spaceBetween',
					controls = [
						ft.Container(
							content = ft.Container(
								on_click=lambda _: page.go("/"),
								width = 20,
								height = 30,
								padding = ft.padding.only(left = 2),
								content = ft.Text("X", size = 20, color = title_color)		                						
							)
						),
						
						ft.Row(
							controls = [
								ft.Text(value = "AGRI-VEILLE", size = 30, color = title_color, weight = 'bold')
							]
						),
						
						ft.Row(
							controls = [
								ft.Icon(ft.icons.SEARCH, color = title_color),
								ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED, color = title_color),
							]
						)
					]
				),
				
				ft.Container(height = 2),
				
				ft.Container(
					width = 560,
					height = 80,
					padding = ft.padding.only(left = 20, top = 10, right = 20),
					content = ft.Text(value = "Du nouveau dans la categorie {}".format(category), color = title_color, size = 18, weight = 'bold'),
				),
				
				ft.Container(
					height = 480,
					content = news
				),
				
				#-----------------
				
				ft.Container(height = 20),
				
			]
		)
	)
    
    background_page2 = ft.Container(
		width = 360,
		height = 660,
		bgcolor = background_color,
		border_radius = 30,
		content = ft.Column(
			controls = [
					ft.Stack(
						controls = [
							contenu_page2
						]
					)
				]
      		)
		)
    

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Stack(
						controls = [
							background_page1
						]
					),
                    
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.Stack(
							controls = [
								background_page2
							]
						),
                    	
                    ],
                )
            )
            
        page.update()

        

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
	
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.on_route_change = set_categ


ft.app(target=main)
