#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera páginas estáticas por categoría (/categorias/<id>.html) para SEO.
Los datos deben mantenerse alineados manualmente con js/products.js.
"""
import os

AFFILIATE_TAG = "cuantifican0b-21"

CATEGORIES = [
    {"id": "agua", "nombre": "Agua y Potabilización", "icono": "💧",
     "meta": "Filtros de agua, pajitas filtrantes y botellas purificadoras para supervivencia y preparacionismo. Comparativa y consejos para elegir el tuyo.",
     "intro": "El agua es la prioridad número uno en cualquier plan de preparacionismo: sin ella, la supervivencia se cuenta en días, no en semanas. Aquí reunimos filtros de agua portátiles, pajitas filtrantes y botellas con filtro integrado pensadas para camping, senderismo, emergencias domésticas o situaciones de desabastecimiento, junto con los consejos prácticos que usan los preppers para no quedarse nunca sin agua potable."},
    {"id": "alimentacion", "nombre": "Alimentación de Larga Duración", "icono": "🥫",
     "meta": "Comida liofilizada, raciones de emergencia y alimentos de larga duración para tu despensa de preparacionismo. Hasta 25 años de vida útil.",
     "intro": "Una reserva de alimentos de larga duración es la base de cualquier despensa preparacionista: raciones liofilizadas, comida de emergencia y kits pensados para durar años sin perder valor nutricional. Aquí encontrarás opciones para montar tu propia reserva, ya sea para una emergencia puntual o para varias semanas de autosuficiencia."},
    {"id": "mochilas", "nombre": "Mochilas y Kits de Emergencia (BOB)", "icono": "🎒",
     "meta": "Mochilas de emergencia y kits de supervivencia 72 horas (BOB - Bug Out Bag) listos para salir de casa en minutos.",
     "intro": "La mochila de emergencia, o BOB (Bug Out Bag), es el equipo que te permite salir de casa en minutos con todo lo necesario para sobrevivir al menos 72 horas por tu cuenta. Aquí tienes kits completos y mochilas ya equipadas con botiquín, radio, iluminación y herramientas básicas, además de los consejos clave para adaptarlas a tu situación real."},
    {"id": "botiquin", "nombre": "Botiquín y Primeros Auxilios", "icono": "⛑️",
     "meta": "Botiquines de primeros auxilios completos para casa, coche o mochila de emergencia. Kits militares y compactos.",
     "intro": "Un botiquín bien equipado es imprescindible en cualquier kit de preparacionismo, tanto para el hogar como para el coche o la mochila de emergencia. Reunimos botiquines de distintos tamaños, desde kits compactos hasta maletines completos de primeros auxilios, junto con recomendaciones sobre qué revisar y cómo mantenerlos siempre listos."},
    {"id": "herramientas", "nombre": "Herramientas y Multiherramientas", "icono": "🛠️",
     "meta": "Multiherramientas y navajas de supervivencia: Leatherman y alternativas para tu equipo de preparacionismo.",
     "intro": "Una buena multiherramienta puede sustituir a media caja de herramientas en una situación de emergencia. Aquí tienes una selección que va desde multiherramientas profesionales tipo Leatherman hasta opciones más económicas, todas pensadas para durar y para resolver imprevistos sobre la marcha."},
    {"id": "comunicacion", "nombre": "Radio y Comunicación", "icono": "📻",
     "meta": "Radios de emergencia con manivela y carga solar, AM/FM, para mantenerte informado cuando falla la red eléctrica o móvil.",
     "intro": "Cuando falla la electricidad, internet o la cobertura móvil, una radio de emergencia con manivela o carga solar puede ser tu única fuente de información fiable. Reunimos radios AM/FM portátiles, muchas con linterna LED integrada, pensadas para funcionar sin depender de la red eléctrica."},
    {"id": "refugio", "nombre": "Refugio y Abrigo Térmico", "icono": "🏕️",
     "meta": "Mantas térmicas y sacos de dormir de emergencia para protegerte del frío en situaciones de supervivencia.",
     "intro": "Protegerte del frío es una prioridad que se subestima con facilidad: la hipotermia puede aparecer mucho antes de lo que crees sin el abrigo adecuado. Aquí tienes mantas térmicas de aluminio y sacos de dormir de emergencia, ligeros y compactos, pensados para llevar siempre en tu mochila o en el coche."},
    {"id": "iluminacion", "nombre": "Iluminación y Linternas", "icono": "🔦",
     "meta": "Linternas LED de alta potencia y recargables para emergencias, camping y kits de supervivencia.",
     "intro": "Una buena fuente de luz portátil es de las primeras cosas que se echan en falta en un apagón. Reunimos linternas LED de alta potencia, recargables por USB, pensadas tanto para el día a día como para situaciones de emergencia prolongada."},
    {"id": "fuego", "nombre": "Fuego y Cocina de Campaña", "icono": "🔥",
     "meta": "Hornillos de gas portátiles y equipo de cocina de campaña para preparacionismo, camping y emergencias.",
     "intro": "Poder cocinar y calentar agua es clave en cualquier situación de emergencia prolongada. Aquí tienes hornillos de gas portátiles, compactos y fáciles de transportar, ideales tanto para tu kit de emergencia como para camping o senderismo."},
    {"id": "libros", "nombre": "Libros y Guías de Preparacionismo", "icono": "📚",
     "meta": "Libros y guías de preparacionismo y supervivencia en español: manuales prácticos para aprender a prepararte paso a paso.",
     "intro": "Tener el equipo adecuado es solo la mitad del trabajo: saber usarlo es la otra mitad. Aquí reunimos libros y manuales de preparacionismo y supervivencia, desde guías generalistas para quien empieza hasta manuales de referencia como el clásico SAS Survival Handbook, pensados para acompañar tu equipo con conocimiento real."},
    {"id": "energia", "nombre": "Energía Portátil y Paneles Solares", "icono": "⚡",
     "meta": "Paneles solares plegables, estaciones de energía portátiles y power banks de alta capacidad para cortes de suministro, camping o el coche.",
     "intro": "Sin electricidad, hasta las tareas más simples se complican: cargar el móvil, mantener la nevera portátil o tener luz por la noche. Aquí reunimos paneles solares plegables tipo BigBlue, estaciones de energía portátiles de distintos tamaños y power banks de alta capacidad, pensados para generar y almacenar energía de forma autónoma durante un corte de suministro, un viaje o una acampada."},
]

TIPS = {
    "agua": [
        "Calcula un mínimo de 3-4 litros de agua por persona y día (beber, cocinar e higiene básica) al montar tu reserva de emergencia.",
        "Combina un filtro mecánico con pastillas potabilizadoras de reserva: si el filtro se satura o se rompe, necesitas un plan B.",
        "Si vas a abastecer a más de una persona, una botella o bolsa con filtro rinde más que una simple pajita filtrante.",
        "Rota el agua embotellada almacenada cada 6-12 meses y anota la fecha de compra en el envase.",
    ],
    "alimentacion": [
        "Aplica el sistema FIFO (\"primero en entrar, primero en salir\"): coloca la comida nueva detrás y consume primero la más antigua.",
        "Calcula un mínimo orientativo de 2.000 kcal por persona y día para tu reserva de emergencia.",
        "Combina alimentos liofilizados (ligeros, larga duración) con conservas y legumbres, más económicas y fáciles de rotar en el día a día.",
        "Prueba las raciones en casa antes de depender de ellas: comprueba que te sientan bien y que sabes prepararlas.",
        "Guarda siempre un abrelatas manual junto a la comida: sin electricidad, muchos abrelatas eléctricos no sirven de nada.",
    ],
    "mochilas": [
        "Sigue la regla de las 72 horas: tu mochila de emergencia (BOB) debe darte autonomía real durante al menos tres días.",
        "Distribuye el peso con cuidado: objetos pesados cerca de la espalda y centrados, los más ligeros arriba o en bolsillos exteriores.",
        "Revisa y actualiza el contenido cada 6 meses: caducidad de alimentos y medicinas, cambios de temporada, ropa que ya no talla.",
        "Adapta el kit a tu núcleo familiar real: medicación crónica, niños pequeños o mascotas cambian por completo lo que necesitas llevar.",
        "Pruébate la mochila cargada al menos una vez antes de necesitarla: el peso \"sobre el papel\" y el peso real casi nunca coinciden.",
    ],
    "botiquin": [
        "Un botiquín genérico no sustituye tu medicación personal: añade siempre la tuya, con receta y en su envase original.",
        "Revisa las fechas de caducidad cada 6 meses, sobre todo antisépticos, analgésicos y apósitos estériles.",
        "El material no sirve de mucho sin saber usarlo: un curso básico de primeros auxilios (RCP, control de hemorragias) es tan importante como el botiquín en sí.",
        "Guarda una copia de tu cartilla de vacunación y alergias dentro del botiquín, en una funda impermeable.",
        "Las vendas y gasas suelen agotarse primero en una emergencia real: lleva más cantidad de la que crees necesaria.",
    ],
    "herramientas": [
        "Una sola multiherramienta de calidad suele rendir más que varias herramientas sueltas de baja calidad.",
        "Aprende a afilar tu navaja o multiherramienta: una hoja desafilada obliga a hacer más fuerza y es más peligrosa que una bien afilada.",
        "Comprueba la normativa local sobre longitud de hoja antes de llevar una navaja o multiherramienta fuera de casa.",
        "Engrasa las articulaciones de forma periódica para que no se agarroten con el uso, la humedad o el paso del tiempo.",
    ],
    "comunicacion": [
        "Ten siempre una fuente de energía manual (manivela o solar) como respaldo para cuando fallen las baterías y la red eléctrica.",
        "Apunta de antemano las frecuencias de emergencia y protección civil de tu zona; en plena crisis no es el momento de buscarlas.",
        "En un apagón, la radio analógica AM/FM suele seguir funcionando cuando internet y la red móvil ya han caído.",
        "Lleva pilas de repuesto aunque tu radio sea solar o de manivela: el sol y el movimiento no siempre bastan para cargarla a tiempo.",
    ],
    "refugio": [
        "Ten en cuenta la regla de las 3 horas: sin refugio ni protección térmica adecuada, la hipotermia puede aparecer en menos de tres horas en condiciones adversas.",
        "Las mantas térmicas de aluminio son ligerísimas pero pensadas para un uso puntual: si vas a necesitar el equipo varias noches, un saco vivac más resistente aguanta mejor.",
        "Combina capas: algo aislante bajo el cuerpo para no perder calor por el suelo, y manta o saco por encima.",
        "Guarda el refugio en una bolsa impermeable aparte, para que esté siempre seco y accesible cuando lo necesites.",
    ],
    "iluminacion": [
        "Lleva siempre dos fuentes de luz independientes: una principal y otra de repuesto, para no depender de una sola batería.",
        "Prioriza linternas recargables por USB, dinamo o solar frente a las de pilas no recargables: reduces tu dependencia de suministro externo.",
        "Guarda las pilas fuera del dispositivo si no vas a usarlo en mucho tiempo, para evitar que se corroan y lo estropeen.",
        "Un frontal (headlamp) libera las manos y suele ser más práctico que una linterna de mano en una emergencia real.",
    ],
    "fuego": [
        "Ten siempre dos métodos de encendido distintos (por ejemplo, mechero y yesquero/pedernal) por si uno falla o se moja.",
        "Nunca uses un hornillo de gas en espacios cerrados sin ventilación: existe riesgo real de intoxicación por monóxido de carbono.",
        "Guarda los cartuchos de gas en un lugar fresco, alejados de cualquier fuente de calor directo.",
        "Practica montar y encender tu hornillo en casa, con calma, antes de tener que depender de él de verdad.",
    ],
    "libros": [
        "No necesitas leerte una biblioteca entera: empieza por una guía generalista y profundiza después en los temas que más te interesen (agua, primeros auxilios, autosuficiencia...).",
        "Prioriza los manuales con procedimientos claros paso a paso frente a los que solo dan teoría: en una emergencia real necesitas poder consultarlos rápido.",
        "Guarda al menos una guía en papel dentro de tu mochila de emergencia: si falla la electricidad o el móvil, un libro físico sigue funcionando.",
        "Complementa la teoría con práctica real: monta el hornillo, arma el botiquín o prueba el nudo antes de necesitarlo de verdad.",
        "Desconfía de manuales que prometen soluciones milagrosas o técnicas de riesgo sin avisos de seguridad; prioriza autores y editoriales con trayectoria contrastada.",
    ],
    "energia": [
        "Calcula tus vatios-hora (Wh) reales antes de comprar: suma el consumo de tus aparatos imprescindibles y elige una batería o power bank con margen, no el modelo mínimo justo.",
        "Un panel solar plegable rinde mucho menos con nubes o mala orientación: no lo cuentes como única fuente de carga, combínalo con una batería ya cargada de reserva.",
        "Carga y descarga tus power banks y estaciones de energía cada pocos meses aunque no los uses: las baterías de litio se degradan igual estando paradas.",
        "Reparte la energía: un power bank pequeño para el móvil y una estación más grande para lo esencial de casa cubren mejor un corte largo que un único aparato grande.",
    ],
}

PRODUCTS = [
    {"asin": "B0DT99W4MK", "foto": "photo-1624520629915-b0e93365c56f", "categoria": "agua", "titulo": "Katadyn BeFree AC 1,0L Black — Filtro de agua para supervivencia y mochileros", "descripcion": "Filtro o sistema de purificación de agua que elimina bacterias, protozoos o partículas en suspensión para obtener agua potable a partir de fuentes naturales. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "10,7l. x 7,8an. x 27,3al. centímetros", "Capacidad": "1 Litros", "Peso": "85 g", "Marca": "KATADYN"} },
    {"asin": "B0DMJCF85X", "foto": "photo-1599490255484-e08a364b4975", "categoria": "agua", "titulo": "Pajita Filtrante 1000 L para Camping, Senderismo y Supervivencia", "descripcion": "Filtro o sistema de purificación de agua que elimina bacterias, protozoos o partículas en suspensión para obtener agua potable a partir de fuentes naturales. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "14l. x 1,8an. x 1,8al. centímetros", "Capacidad": "50 Mililitros", "Peso": "21 g", "Marca": "joypur"} },
    {"asin": "B0H1XQ5TYJ", "foto": "photo-1568395216634-ab1b1e848751", "categoria": "agua", "titulo": "Botella con Filtro Purificador de Agua por Prensado Manual", "descripcion": "Filtro o sistema de purificación de agua que elimina bacterias, protozoos o partículas en suspensión para obtener agua potable a partir de fuentes naturales. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "8l. x 8an. x 24al. centímetros", "Capacidad": "500 Mililitros", "Peso": "375 g", "Marca": "KANDURO"} },
    {"asin": "B00GOPHOSQ", "foto": "photo-1732667000298-31b28094ac1e", "categoria": "agua", "titulo": "Aquatabs 8,5 mg — 50 Pastillas Potabilizadoras de Agua", "descripcion": "Pastillas potabilizadoras que desinfectan el agua mediante un tratamiento químico, sin necesidad de electricidad ni piezas mecánicas. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "12,9l. x 1,8an. x 4,8al. centímetros", "Capacidad": "1 Litros", "Peso": "10 g", "Marca": "Aquatabs"} },
    {"asin": "B0GMXX2G9S", "foto": "photo-1643114455894-d7a4cd35c395", "categoria": "agua", "titulo": "AWAKING Pastillas Potabilizadoras de Agua, 48 uds — tratamiento hasta 9.600 litros", "descripcion": "Pastillas potabilizadoras que desinfectan el agua mediante un tratamiento químico, sin necesidad de electricidad ni piezas mecánicas. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "10,5l. x 10,5an. x 12al. centímetros", "Peso": "180 g", "Marca": "PLANTAWA"} },
    {"asin": "B0DM8FNFL5", "foto": "photo-1789925941122-8162d3628b47", "categoria": "agua", "titulo": "VEVOR Sistema de Filtración de Agua por Gravedad 8,5L, acero inoxidable, para uso familiar", "descripcion": "Filtro o sistema de purificación de agua que elimina bacterias, protozoos o partículas en suspensión para obtener agua potable a partir de fuentes naturales. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "28,5l. x 28,5an. x 64,2al. centímetros", "Capacidad": "2,25 Galones", "Peso": "3,5 kg", "Marca": "VEVOR"} },
    {"asin": "B08ZYMXLMH", "foto": "photo-1653543362966-a97e081f3086", "categoria": "agua", "titulo": "Membrane Solutions Sistema de Filtro de Agua Portátil por Gravedad, con bolsa de 6L", "descripcion": "Filtro o sistema de purificación de agua que elimina bacterias, protozoos o partículas en suspensión para obtener agua potable a partir de fuentes naturales. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "9,9l. x 5,8an. x 26,9al. centímetros", "Capacidad": "6 Litros", "Peso": "363 g", "Marca": "Membrane Solutions"} },
    {"asin": "B0F3D422BK", "foto": "photo-1519040364483-542d88b34646", "categoria": "agua", "titulo": "Waterflow Filtro de Agua de 3 Fases para Excursionistas y Kit de Supervivencia", "descripcion": "Filtro o sistema de purificación de agua que elimina bacterias, protozoos o partículas en suspensión para obtener agua potable a partir de fuentes naturales. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "35l. x 35an. x 155al. milímetros", "Capacidad": "8000 Litros", "Peso": "110 g", "Marca": "Hesago"} },
    {"asin": "B0DXQ1QPSL", "foto": "photo-1624361919151-0d76b3f6910a", "categoria": "agua", "titulo": "HOTUT Mini Filtro de Agua Personal 1500L, pack de 2 unidades portátiles", "descripcion": "Filtro o sistema de purificación de agua que elimina bacterias, protozoos o partículas en suspensión para obtener agua potable a partir de fuentes naturales. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Dimensiones": "27,6l. x 16,5an. x 4,2al. centímetros", "Capacidad": "4000 Litros", "Peso": "300 g", "Marca": "HOTUT"} },
    {"asin": "B0DJVY6JTW", "foto": "photo-1730266450574-93849758efb7", "categoria": "agua", "titulo": "Botella Plegable 1000ml con Filtro de 0,01µm, hasta 5.000 litros de agua filtrada", "descripcion": "Filtro o sistema de purificación de agua que elimina bacterias, protozoos o partículas en suspensión para obtener agua potable a partir de fuentes naturales. Pensado para potabilizar o filtrar agua durante una emergencia, un corte de suministro o una salida al aire libre.", "atributos": {"Marca": "joypur", "Peso": "150 g", "Dimensiones": "11an. x 6,5al. centímetros"} },
    {"asin": "B004JT7F8I", "foto": "photo-1775626093977-a1f9051b99d2", "categoria": "alimentacion", "titulo": "ReadyWise 120 raciones — Almuerzo y cena, 13 recetas, hasta 25 años de vida útil", "descripcion": "Ración de comida de larga duración, lista para preparar con agua caliente o fría, pensada para reservas de alimentación de emergencia. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {"Marca": "ReadyWise", "Dimensiones": "38,1 x 25,4 x 30,5 centímetros", "Peso": "6,6 kg"} },
    {"asin": "B08C9JZYPG", "foto": "photo-1720672284707-bc62c5f9cc9a", "categoria": "alimentacion", "titulo": "ReadyWise 60 raciones — Desayuno, comida y cena, bolsa Grab & Go liofilizada", "descripcion": "Ración de comida de larga duración, lista para preparar con agua caliente o fría, pensada para reservas de alimentación de emergencia. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {"Marca": "ReadyWise", "Peso": "1,36 kg"} },
    {"asin": "B0GVG47NB5", "foto": "photo-1765524394295-f36d3e88a7a8", "categoria": "alimentacion", "titulo": "Ración de comida de emergencia para supervivencia y protección civil", "descripcion": "Ración de comida de larga duración, lista para preparar con agua caliente o fría, pensada para reservas de alimentación de emergencia. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {"Marca": "Lebenskraft", "Peso": "2,5 kg", "Tamaño": "2.5 kg"} },
    {"asin": "B0CKJ1G7GD", "foto": "photo-1757179096076-29c90da4a9cb", "categoria": "alimentacion", "titulo": "MRE-9 Ración de emergencia — 20 años de vida útil, vitaminas extra, 24 x 500 g", "descripcion": "Ración de comida de larga duración, lista para preparar con agua caliente o fría, pensada para reservas de alimentación de emergencia. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {"Marca": "MRE-9", "Peso": "12 kg", "Tamaño": "500 gram per stuk"} },
    {"asin": "B084L14VKD", "foto": "photo-1757179096076-29c90da4a9cb", "categoria": "alimentacion", "titulo": "Paquete de ración de 24 horas del ejército militar francés MRE (pack de 3)", "descripcion": "Ración de comida de larga duración, lista para preparar con agua caliente o fría, pensada para reservas de alimentación de emergencia. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {"Marca": "RCIR", "Tamaño": "No"} },
    {"asin": "B071R95ZTV", "foto": "photo-1693996046865-19217d179161", "categoria": "alimentacion", "titulo": "Trek'n Eat Leche Entera en Polvo — leche instantánea con 15 años de vida útil", "descripcion": "Leche en polvo de larga conservación, pensada como reserva nutricional de fácil almacenamiento. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {"Marca": "KATADYN", "Peso": "780 g", "Tamaño": "650 g (1er Pack)"} },
    {"asin": "B08D9WVXNG", "foto": "photo-1596151163116-98a5033814c2", "categoria": "alimentacion", "titulo": "Nutrient Survival Leche en Polvo con Vitaminas — suministro de preparación liofilizado", "descripcion": "Leche en polvo de larga conservación, pensada como reserva nutricional de fácil almacenamiento. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {"Marca": "Nutrient Survival", "Peso": "28,3 g", "Tamaño": "1,48,9 g (1 unidad)"} },
    {"asin": "B0917PD1QY", "foto": "photo-1591857177580-dc82b9ac4e1e", "categoria": "alimentacion", "titulo": "Kit de Semillas de Huerto Urbano, 12 vegetales — 5.100 semillas ecológicas para autosuficiencia", "descripcion": "Kit de semillas para huerto propio, orientado a quienes buscan una fuente de alimento más autosuficiente a medio plazo. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {} },
    {"asin": "B0G262DNB9", "foto": "photo-1647553756926-21a62021b9d2", "categoria": "alimentacion", "titulo": "Kit de 24 Variedades de Semillas de Huerto y Hierbas Aromáticas, 13.800 semillas", "descripcion": "Kit de semillas para huerto propio, orientado a quienes buscan una fuente de alimento más autosuficiente a medio plazo. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {} },
    {"asin": "B0DYHFQW4Z", "foto": "photo-1690983318341-598b223c6560", "categoria": "alimentacion", "titulo": "Galletas de Emergencia de 20 años de vida útil, 6.840 kcal, 12 bolsas, sabor cacahuete", "descripcion": "Galletas energéticas de muy larga conservación, pensadas como ración calórica compacta de emergencia. Pensado para formar parte de una reserva de alimentos de larga duración ante posibles cortes de suministro.", "atributos": {"Peso": "1,61 kg", "Tamaño": "120g"} },
    {"asin": "B0F75GGNZT", "foto": "photo-1624638760852-8ede1666ab07", "categoria": "mochilas", "titulo": "Kit de Supervivencia Completo 72 Horas — Camping gas, botiquín táctico, radio solar", "descripcion": "Kit multiusos que agrupa varios elementos básicos de supervivencia (luz, calor, primeros auxilios o comunicación) en un mismo paquete. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Marca": "Humpti", "Dimensiones": "53 x 40 x 35 centímetros", "Peso": "700 g"} },
    {"asin": "B0FL1WWR5Q", "foto": "photo-1596055746427-d5f61aa5df99", "categoria": "mochilas", "titulo": "Gemmac Kit Supervivencia 140 en 1 — Botiquín, radio a pilas, linterna", "descripcion": "Kit multiusos que agrupa varios elementos básicos de supervivencia (luz, calor, primeros auxilios o comunicación) en un mismo paquete. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Marca": "Gemmac", "Dimensiones": "19 x 16 x 15 centímetros", "Peso": "2 kg"} },
    {"asin": "B07GGPH3CZ", "foto": "photo-1714384716870-6d6322bf5a7f", "categoria": "mochilas", "titulo": "ProCase 40L Mochila Táctica Militar MOLLE — para BOB, caza y senderismo", "descripcion": "Mochila táctica de gran capacidad, pensada como base de una mochila de emergencia (BOB) o para uso en exteriores exigentes. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Tamaño": "19,68 Pulgadas", "Marca": "ProCase", "Peso": "56,6 g", "Dimensiones": "35,6f. x 30,5an. x 10,2al. centímetros"} },
    {"asin": "B08NF9KH46", "foto": "photo-1758618851341-35cfd04b5406", "categoria": "mochilas", "titulo": "QT&QY Mochila Militar Táctica 45L MOLLE — Bug Out Bag de 3 días", "descripcion": "Mochila táctica de gran capacidad, pensada como base de una mochila de emergencia (BOB) o para uso en exteriores exigentes. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Tamaño": "17 Pulgadas", "Marca": "QT&QY", "Peso": "1,36 kg", "Dimensiones": "29f. x 33an. x 45al. centímetros"} },
    {"asin": "B00149O23M", "foto": "photo-1624638764471-cffef5035746", "categoria": "mochilas", "titulo": "Ready America Mochila de Emergencia — kit preparado para terremotos y desastres", "descripcion": "Mochila de emergencia preparada de fábrica, pensada como kit inicial ante terremotos u otros desastres. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Marca": "Ready America", "Dimensiones": "25,4 x 27,9 x 35,6 centímetros", "Peso": "4,44 kg"} },
    {"asin": "B0F47YJ2KC", "foto": "photo-1771241137542-c27f466b2a81", "categoria": "mochilas", "titulo": "ZHIERNA Riñonera Táctica MOLLE para cinturón, complemento para mochila de emergencia", "descripcion": "Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Marca": "ZHIERNA", "Tamaño": "7,8\"-12,6\" B x 5,9\" H x 5,0\"-5,12\"D", "Dimensiones": "20l. x 13an. x 15al. centímetros", "Peso": "340 g"} },
    {"asin": "B0DCHC34XW", "foto": "photo-1776687773939-348819a9b787", "categoria": "mochilas", "titulo": "TSPRO Bolsa Táctica MOLLE Dump Pouch plegable para cinturón o mochila", "descripcion": "Riñonera o bolsa táctica modular (sistema MOLLE) para llevar objetos pequeños de forma accesible. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Marca": "TSPRO", "Dimensiones": "10,2l. x 3,8an. x 10,2al. centímetros", "Peso": "118 g"} },
    {"asin": "B0BDK85L3T", "foto": "photo-1509762774605-f07235a08f1f", "categoria": "mochilas", "titulo": "CAMELBAK Mochila de Hidratación Classic 4L con depósito de 2L", "descripcion": "Sistema de hidratación con depósito de agua integrado, pensado para llevar líquido de forma cómoda durante desplazamientos a pie. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Marca": "CAMELBAK", "Peso": "408 g", "Dimensiones": "23an. x 15,7al. centímetros"} },
    {"asin": "B09B3HG12T", "foto": "photo-1784194311259-cba7ed160f36", "categoria": "mochilas", "titulo": "YUMQUA Bolsa Estanca Impermeable Dry Bag, varias capacidades, para mantener el equipo seco", "descripcion": "Bolsa estanca impermeable pensada para mantener seco el equipo en condiciones de lluvia o cerca del agua. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Marca": "YUMQUA", "Peso": "270 g", "Tamaño": "5L"} },
    {"asin": "B07Y2VFPS1", "foto": "photo-1752392185223-c1d5d5f1d7af", "categoria": "mochilas", "titulo": "Unigear Bolsa de Agua para Mochila de Hidratación, libre de BPA", "descripcion": "Sistema de hidratación con depósito de agua integrado, pensado para llevar líquido de forma cómoda durante desplazamientos a pie. Pensado para completar una mochila de emergencia (BOB) o un kit de supervivencia de 72 horas.", "atributos": {"Marca": "Unigear", "Peso": "230 g"} },
    {"asin": "B09W2WWZGY", "foto": "photo-1563260324-5ebeedc8af7c", "categoria": "botiquin", "titulo": "Botiquín maletín mediano de primeros auxilios, doble cierre de seguridad", "descripcion": "Botiquín con material de primeros auxilios organizado en un maletín o bolsa de transporte. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "Sumedtec", "Peso": "1 kg"} },
    {"asin": "B07R3RMFC4", "foto": "photo-1566889035559-b14ef9d4c365", "categoria": "botiquin", "titulo": "HONYAO Botiquín de Primeros Auxilios 200 piezas, mini kit de supervivencia", "descripcion": "Botiquín con material de primeros auxilios organizado en un maletín o bolsa de transporte. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "HONYAO", "Peso": "420 g", "Dimensiones": "20 x 13 x 5 centímetros"} },
    {"asin": "B0BDGCLB3C", "foto": "photo-1566889035559-b14ef9d4c365", "categoria": "botiquin", "titulo": "Botiquín maletín grande de primeros auxilios, kit militar para coche y mochila", "descripcion": "Botiquín con material de primeros auxilios organizado en un maletín o bolsa de transporte. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "Sumedtec", "Peso": "2,4 kg"} },
    {"asin": "B0DNLPG9CZ", "foto": "photo-1776687773955-17135a5cff90", "categoria": "botiquin", "titulo": "Thulander Pack 2 Torniquetes Tácticos + 2 Vendajes Israelíes para hemorragias", "descripcion": "Botiquín con material de primeros auxilios organizado en un maletín o bolsa de transporte. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "Genérico", "Peso": "180 g", "Dimensiones": "26 x 18 x 2,5 centímetros"} },
    {"asin": "B0F4RBK2W3", "foto": "photo-1564144573017-8dc932e0039e", "categoria": "botiquin", "titulo": "NUVEXIA Botiquín de Primeros Auxilios Premium 300 piezas para coche y viaje", "descripcion": "Botiquín con material de primeros auxilios organizado en un maletín o bolsa de transporte. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "NUVEXIA", "Peso": "400 g", "Dimensiones": "21 x 13 x 5 centímetros"} },
    {"asin": "B0BWY1JBL9", "foto": "photo-1769430534842-b249cd217ecc", "categoria": "botiquin", "titulo": "RHINO RESCUE Kit Individual de Control de Hemorragias IFAK, botiquín militar de trauma", "descripcion": "Botiquín con material de primeros auxilios organizado en un maletín o bolsa de transporte. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "RHINO RESCUE", "Peso": "470 g"} },
    {"asin": "B0CNXKWNBQ", "foto": "photo-1776046982340-653e492c5436", "categoria": "botiquin", "titulo": "Vendaje de Trauma de Emergencia Vent Chest Seal, pack de 2 unidades", "descripcion": "Apósito sellante para heridas torácicas, pensado como material de primera respuesta ante traumatismos. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "JCRWXP", "Peso": "70 g"} },
    {"asin": "B0CYCRVMW5", "foto": "photo-1684248655527-46bee8e79029", "categoria": "botiquin", "titulo": "Health Press Vendas de Gasa Elástica, pack de 20 rollos", "descripcion": "Venda o gasa elástica para la sujeción de apósitos y compresas en curas de primeros auxilios. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "Health Press", "Tamaño": "8 cm x 4 m", "Dimensiones": "8 x 3 x 3 centímetros", "Peso": "230 g"} },
    {"asin": "B0B6427ND9", "foto": "photo-1633002161416-8e2fafa0996b", "categoria": "botiquin", "titulo": "Peha-Haft Venda Elástica Autoadhesiva y Cohesiva para sujeción de gasas", "descripcion": "Venda o gasa elástica para la sujeción de apósitos y compresas en curas de primeros auxilios. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "Peha-haft", "Tamaño": "4mx6cm", "Peso": "20 g"} },
    {"asin": "B08LJCN9PF", "foto": "photo-1625465586827-28f3fa53ae43", "categoria": "botiquin", "titulo": "AIESI Collarín Cervical Ajustable en 4 posiciones EasyLock, inmovilización de cuello", "descripcion": "Collarín cervical ajustable para la inmovilización del cuello ante una sospecha de lesión. Pensado para completar un botiquín doméstico, de viaje o de emergencia.", "atributos": {"Marca": "AIESI", "Tamaño": "Adulto", "Peso": "130 g"} },
    {"asin": "B0777HG5ZB", "foto": "photo-1662220658953-880fe3c763a7", "categoria": "herramientas", "titulo": "Leatherman Signal — Multiherramienta de supervivencia", "descripcion": "Multiherramienta plegable que combina varias funciones (alicates, hoja, destornilladores) en un único cuerpo compacto. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {"Marca": "Leatherman", "Dimensiones": "13,2 x 9,1 x 5 centímetros", "Peso": "213 g", "Tamaño": "11.43 x 3.81 x 1.6 cm"} },
    {"asin": "B0CX32Q354", "foto": "photo-1607456646689-76a412e200e9", "categoria": "herramientas", "titulo": "Leatherman Skeletool CX — Acero inoxidable, fabricada en EE.UU.", "descripcion": "Multiherramienta plegable que combina varias funciones (alicates, hoja, destornilladores) en un único cuerpo compacto. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {"Marca": "Leatherman", "Dimensiones": "10,2 x 3,1 x 1,3 centímetros", "Peso": "142 g", "Tamaño": "10 cm"} },
    {"asin": "B095LVRVMZ", "foto": "photo-1613178594694-5f96ae9b5bb0", "categoria": "herramientas", "titulo": "BIBURY Multiherramienta de alicates y navaja multiusos con bloqueo de seguridad", "descripcion": "Multiherramienta plegable que combina varias funciones (alicates, hoja, destornilladores) en un único cuerpo compacto. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {"Marca": "BIBURY", "Dimensiones": "5,2 x 2 x 16,5 centímetros", "Peso": "265 g", "Tamaño": "Circa 15 x 5 x 2 cm (circa 6 x 2 x 0.8 pollici)"} },
    {"asin": "B0G2RVVKPS", "foto": "photo-1592066020953-4b41cc1e6d00", "categoria": "herramientas", "titulo": "BIBURY Multiherramienta de titanio y acero damasco con navaja de supervivencia", "descripcion": "Multiherramienta plegable que combina varias funciones (alicates, hoja, destornilladores) en un único cuerpo compacto. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {"Marca": "BIBURY", "Dimensiones": "11,5 x 4,2 x 2,5 centímetros", "Peso": "320 g", "Tamaño": "11.5 cm x 4.2 cm x 2.5 cm"} },
    {"asin": "B09WHFTYH2", "foto": "photo-1640045444503-23b8e10032cb", "categoria": "herramientas", "titulo": "Pala Plegable Multifuncional 58 cm, herramienta militar de supervivencia", "descripcion": "Pala plegable multifunción pensada para tareas de campo, excavación ligera o emergencias en el vehículo. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {} },
    {"asin": "B0FHX29QR6", "foto": "photo-1677412479532-dd0185413a73", "categoria": "herramientas", "titulo": "KHU Cuchillo Bushcraft de acero D2 con funda Kydex, para caza y supervivencia", "descripcion": "Cuchillo de hoja fija pensado para tareas de corte, caza o bushcraft, con funda de transporte incluida. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {"Marca": "KHU", "Peso": "311 g", "Tamaño": "14 cm"} },
    {"asin": "B0DGGNWMJ4", "foto": "photo-1444228250525-3d441b642d12", "categoria": "herramientas", "titulo": "Hacha Vikinga artesanal de bushcraft para camping y supervivencia", "descripcion": "Hacha de mano pensada para tareas de bushcraft como cortar leña o preparar un refugio improvisado. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {} },
    {"asin": "B000QD1726", "foto": "photo-1622768503544-c2880f70f89c", "categoria": "herramientas", "titulo": "BAHCO Serrucho Plegable de baja fricción — sierra de bushcraft y poda", "descripcion": "Serrucho plegable de poda, útil para cortar ramas o madera de pequeño diámetro en el campo. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {} },
    {"asin": "B0F98Q4BMN", "foto": "photo-1633476211332-fc83161ba682", "categoria": "herramientas", "titulo": "Brotree Paracord 550 de 4mm, 10m, 7 hebras — cuerda de nylon multiusos", "descripcion": "Cuerda de nylon multiusos (paracord), útil para atar, reparar o improvisar equipo en el exterior. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {"Marca": "Brotree", "Peso": "100 g"} },
    {"asin": "B0CG23K1TF", "foto": "photo-1680538993961-bac6596bc13e", "categoria": "herramientas", "titulo": "BOMEI PACK 2 Rollos de Cinta Americana 50mm x 50m, reforzada y resistente", "descripcion": "Cinta adhesiva de alta resistencia, útil para reparaciones rápidas de equipo, calzado o refugios improvisados. Una herramienta pensada para tareas de campo, bushcraft o mantenimiento en situaciones de autosuficiencia.", "atributos": {"Marca": "BOMEI PACK", "Peso": "980 g", "Dimensiones": "2Grosor milímetros"} },
    {"asin": "B09KNPHP9W", "foto": "photo-1552172904-faeb4b22ff9a", "categoria": "comunicacion", "titulo": "Radio Solar de manivela portátil Dynamo AM/FM con linterna LED", "descripcion": "Radio de emergencia con carga solar y/o de manivela, pensada para seguir informado cuando falla la electricidad. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Potencia": "3 Watios", "Marca": "SOLARBABY", "Dimensiones": "10,2l. x 17,8an. x 8,9al. centímetros", "Peso": "28 g"} },
    {"asin": "B0GSQJ7KRG", "foto": "photo-1556009148-ed88760014c4", "categoria": "comunicacion", "titulo": "Radio de Emergencia Portátil AM/FM con solar recargable y dinamo de manivela", "descripcion": "Radio de emergencia con carga solar y/o de manivela, pensada para seguir informado cuando falla la electricidad. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Dimensiones": "15l. x 5an. x 4al. centímetros", "Peso": "230 g", "Marca": "Gemmac"} },
    {"asin": "B0F6MQGN4D", "foto": "photo-1749649773867-9c9787a47df9", "categoria": "comunicacion", "titulo": "Radio Solar de Emergencia AM/FM con manivela y batería recargable", "descripcion": "Radio de emergencia con carga solar y/o de manivela, pensada para seguir informado cuando falla la electricidad. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Dimensiones": "17,3l. x 12,1an. x 7,4al. centímetros", "Peso": "850 g", "Marca": "Mesqool"} },
    {"asin": "B0FNQP8G4W", "foto": "photo-1586374579268-e08642454549", "categoria": "comunicacion", "titulo": "Gaswei G1Pro+ Walkie Talkie de Largo Alcance Profesional, resistente IP67", "descripcion": "Walkie talkie de largo alcance para mantener la comunicación con el grupo sin depender de la red móvil. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Marca": "Gaswei", "Peso": "190 g"} },
    {"asin": "B0GT8SG24D", "foto": "photo-1739268984311-b478fccf256e", "categoria": "comunicacion", "titulo": "ADDTOP Cargador Solar Power Bank 20.000 mAh con carga rápida USB-C", "descripcion": "Cargador solar con batería incorporada para recargar teléfonos y pequeños dispositivos sin depender de la red eléctrica. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Capacidad": "20000 Miliamperios hora (mAh)", "Peso": "450 g", "Dimensiones": "29l. x 89an. x 176Grosor milímetros"} },
    {"asin": "B0H3TGS56C", "foto": "photo-1719251295805-6ea14bb06bef", "categoria": "comunicacion", "titulo": "Gosknor Silbato de Emergencia de Titanio, para señalización y rescate", "descripcion": "Silbato de emergencia de alta audibilidad, pensado para pedir ayuda o hacerse localizar en caso de pérdida o accidente. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {} },
    {"asin": "B0CQ32DRNT", "foto": "photo-1554341543-6eb780242777", "categoria": "comunicacion", "titulo": "RiToEasysports Espejo de Señales de Supervivencia, reflector multifuncional de rescate", "descripcion": "Espejo de señales para reflejar la luz solar y hacerse visible a distancia en una situación de rescate. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Marca": "‎RiToEasysports", "Peso": "‎37 g"} },
    {"asin": "B0DBM5G2VQ", "foto": "photo-1598984040075-8ef2c799bbba", "categoria": "comunicacion", "titulo": "McMurdo FastFind 220 — Baliza de rescate personal (PLB) vía satélite, sin suscripción", "descripcion": "Baliza de rescate personal (PLB) que envía la posición vía satélite en una emergencia, sin depender de cobertura móvil. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Marca": "OSAT", "Peso": "440 g"} },
    {"asin": "B0H6JT7V11", "foto": "photo-1517408395525-fa05dd0bb2ef", "categoria": "comunicacion", "titulo": "Denver Radio Portátil Recargable, radio solar de emergencia con manivela", "descripcion": "Radio de emergencia con carga solar y/o de manivela, pensada para seguir informado cuando falla la electricidad. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Dimensiones": "9,7l. x 6,8an. x 17,5al. centímetros", "Peso": "250 g", "Marca": "Denver"} },
    {"asin": "B0GYZ9R1FQ", "foto": "photo-1645391986480-7c13dde82793", "categoria": "comunicacion", "titulo": "SOLARBABY Radio de Emergencia DAB+/FM con Power Bank de 20.000 mAh integrado", "descripcion": "Radio de emergencia con carga solar y/o de manivela, pensada para seguir informado cuando falla la electricidad. Pensado para mantener la comunicación, la señalización o la carga de dispositivos cuando fallan la red eléctrica o la cobertura móvil.", "atributos": {"Potencia": "3 Watios", "Dimensiones": "17,8l. x 6,4an. x 8,6al. centímetros", "Peso": "738 g", "Marca": "SOLARBABY"} },
    {"asin": "B09GM8XJ3M", "foto": "photo-1759997725476-850059175ece", "categoria": "refugio", "titulo": "HONYAO Saco de dormir de emergencia, manta térmica de aluminio", "descripcion": "Saco o manta térmica de aislamiento ligero, pensado para conservar el calor corporal en una emergencia o vivac improvisado. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {"Dimensiones": "2,1l. x 0,9an. metros", "Peso": "110 g", "Tamaño": "213_x_91_cm", "Marca": "HONYAO"} },
    {"asin": "B09GMCTMQC", "foto": "photo-1558477280-1bfed08ea5db", "categoria": "refugio", "titulo": "HONYAO Saco de dormir de emergencia tipo Bivy para supervivencia", "descripcion": "Saco o manta térmica de aislamiento ligero, pensado para conservar el calor corporal en una emergencia o vivac improvisado. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {} },
    {"asin": "B0F7KYSVBM", "foto": "photo-1708105559945-ad5d6612c78c", "categoria": "refugio", "titulo": "Deecam Saco de dormir de emergencia, aislamiento térmico ligero", "descripcion": "Saco o manta térmica de aislamiento ligero, pensado para conservar el calor corporal en una emergencia o vivac improvisado. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {"Marca": "Deecam", "Dimensiones": "2,1l. x 1an. metros", "Tamaño": "2 Camuflaje 210×100cm"} },
    {"asin": "B0BH48615L", "foto": "photo-1633805159007-8e198bbcc931", "categoria": "refugio", "titulo": "LYN Tienda de Campaña Instantánea, impermeable y ligera para emergencia y supervivencia", "descripcion": "Tienda de campaña ligera, pensada como refugio temporal en acampada o en una situación de emergencia. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {"Dimensiones": "2,08l. x 0,92an. x 0,8al. metros", "Peso": "714 g", "Tamaño": "L"} },
    {"asin": "B07WR1V29Y", "foto": "photo-1576176539998-0237d1ac6a85", "categoria": "refugio", "titulo": "Night Cat Tienda de Campaña para 1-2 Personas, impermeable y de montaje fácil", "descripcion": "Tienda de campaña ligera, pensada como refugio temporal en acampada o en una situación de emergencia. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {"Dimensiones": "2,2l. x 1,4an. x 1,2al. metros", "Peso": "2,49 kg", "Tamaño": "2 Persona"} },
    {"asin": "B0DXVJM334", "foto": "photo-1698731048404-1c12d7189e48", "categoria": "refugio", "titulo": "Yuzonc Colchoneta Camping Ultraligera, aislante y compacta para dormir en emergencias", "descripcion": "Colchoneta hinchable o aislante que evita la pérdida de calor por contacto con el suelo al dormir. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {"Marca": "Yuzonc", "Tamaño": "200 x 67 x 15 cm", "Peso": "900 g", "Dimensiones": "200 x 67 x 11,5 centímetros"} },
    {"asin": "B0CSPBYYJD", "foto": "photo-1771933270678-a97631ae9311", "categoria": "refugio", "titulo": "Toldo de Camping 3x3m Impermeable, protección solar y de lluvia para refugio improvisado", "descripcion": "Tienda de campaña ligera, pensada como refugio temporal en acampada o en una situación de emergencia. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {"Marca": "VOSOIR", "Peso": "850 g", "Dimensiones": "3l. x 3an. metros", "Tamaño": "3x3M"} },
    {"asin": "B08HH7NY9J", "foto": "photo-1445307806294-bff7f67ff225", "categoria": "refugio", "titulo": "AnorTrek Hamaca de Camping con Mosquitero integrado, para refugio en exterior", "descripcion": "Hamaca de camping con mosquitero integrado, pensada como alternativa ligera de refugio nocturno en exterior. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {"Marca": "AnorTrek", "Dimensiones": "2,6l. x 1,4an. metros", "Peso": "790 g", "Tamaño": "80 x 20 x 15 cm"} },
    {"asin": "B01M19HAEB", "foto": "photo-1759997726239-9c319108c100", "categoria": "refugio", "titulo": "Bramble Pack de 10 Mantas Térmicas de Emergencia", "descripcion": "Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {} },
    {"asin": "B0CJT7JW5Z", "foto": "photo-1788768821733-e1119046b09e", "categoria": "refugio", "titulo": "Kit Lona Impermeable 2x3m multiusos, para refugio, cobertizo o protección de equipo", "descripcion": "Lona o toldo impermeable multiusos, útil como refugio improvisado, protección de equipo o cobertizo temporal. Pensado para proteger del frío, el viento o la lluvia en una situación de acampada o emergencia.", "atributos": {"Marca": "moem&an", "Peso": "540 g", "Dimensiones": "3l. x 2an. metros", "Tamaño": "2x3m"} },
    {"asin": "B08MLBPRCS", "foto": "photo-1561916960-dea3b9b0355a", "categoria": "iluminacion", "titulo": "LEKIA Linterna LED de alta potencia recargable por USB, 5 modos", "descripcion": "Linterna recargable de alta potencia, pensada como fuente de luz principal o de repuesto en cortes de suministro o exteriores. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Potencia": "90000 Lumen", "Marca": "LEKIA", "Dimensiones": "185f. x 42an. x 42al. milímetros", "Peso": "205 g"} },
    {"asin": "B0CNKN5YSS", "foto": "photo-1561916828-f1fae4c82ba2", "categoria": "iluminacion", "titulo": "Shadowhawk Linterna LED de alta potencia, recargable, uso táctico", "descripcion": "Linterna recargable de alta potencia, pensada como fuente de luz principal o de repuesto en cortes de suministro o exteriores. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Potencia": "30000 Lumen", "Marca": "Shadowhawk", "Dimensiones": "180f. x 43an. x 43al. milímetros"} },
    {"asin": "B0DXDTB6Q2", "foto": "photo-1580846841980-225e3e2832ae", "categoria": "iluminacion", "titulo": "Linterna LED de alta potencia recargable, batería de 5000 mAh", "descripcion": "Linterna recargable de alta potencia, pensada como fuente de luz principal o de repuesto en cortes de suministro o exteriores. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Potencia": "20000 Lumen", "Marca": "Akdomart", "Dimensiones": "140f. x 20an. x 20al. milímetros"} },
    {"asin": "B09MS489TF", "foto": "photo-1517457773273-412ec74a18cd", "categoria": "iluminacion", "titulo": "POKISEED Linterna Frontal LED Recargable 1500 lúmenes, USB-C 5000 mAh", "descripcion": "Linterna recargable de alta potencia, pensada como fuente de luz principal o de repuesto en cortes de suministro o exteriores. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Potencia": "1500 Lumen", "Dimensiones": "7f. x 15an. x 6al. centímetros", "Peso": "270 g"} },
    {"asin": "B09KRQRRFL", "foto": "photo-1596093019686-550d740a2870", "categoria": "iluminacion", "titulo": "Glocusent Lámpara de Camping, 106 LED, 80 horas de autonomía, recargable USB-C", "descripcion": "Lámpara de camping de gran autonomía, pensada para iluminar una zona amplia durante acampadas o cortes de luz. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Potencia": "1200 Lumen", "Marca": "Glocusent", "Dimensiones": "14,1l. x 5,6an. x 5,6al. centímetros"} },
    {"asin": "B0DGBRL3H2", "foto": "photo-1528351655744-27cc30462816", "categoria": "iluminacion", "titulo": "Sterno Velas de Emergencia, hasta 100 horas de combustión continua", "descripcion": "Velas de larga combustión pensadas como fuente de luz o calor de reserva ante un corte de suministro eléctrico. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Marca": "Sterno", "Dimensiones": "8,9an. x 10,2al. centímetros", "Peso": "2,27 kg"} },
    {"asin": "B0197R8882", "foto": "photo-1597166041385-dccfb3077489", "categoria": "iluminacion", "titulo": "Cyalume SnapLight Barra de Luz Química Verde de 12 horas, señalización de emergencia", "descripcion": "Barra de luz química de un solo uso, útil para señalización o iluminación de emergencia sin necesidad de batería. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Peso": "40 g", "Dimensiones": "21l. x 3an. x 2,5al. centímetros", "Marca": "Cyalume"} },
    {"asin": "B0GGY8TTR2", "foto": "photo-1598096928085-058ac66c24f6", "categoria": "iluminacion", "titulo": "HENGBIRD Set de 4 Linternas Dinamo, sin pilas, carga manual de emergencia", "descripcion": "Linterna recargable de alta potencia, pensada como fuente de luz principal o de repuesto en cortes de suministro o exteriores. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Dimensiones": "15f. x 25an. x 2,5al. centímetros", "Peso": "210 g", "Marca": "HENGBIRD"} },
    {"asin": "B0FXMTMGS8", "foto": "photo-1623048793098-1f9638de7c49", "categoria": "iluminacion", "titulo": "Baliza de Emergencia V16 Homologada DGT, sustituye a los triángulos", "descripcion": "Baliza luminosa de emergencia homologada para señalizar un vehículo averiado en carretera, en sustitución de los triángulos. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Marca": "bip & drive", "Peso": "217 g"} },
    {"asin": "B0F8QFVH8L", "foto": "photo-1476900164809-ff19b8ae5968", "categoria": "iluminacion", "titulo": "Pack de 5 Velas de Supervivencia, hasta 30 horas de combustión cada una", "descripcion": "Velas de larga combustión pensadas como fuente de luz o calor de reserva ante un corte de suministro eléctrico. Una fuente de luz pensada para cortes de suministro eléctrico, acampada o emergencias.", "atributos": {"Dimensiones": "6,3an. centímetros", "Peso": "86,2 g"} },
    {"asin": "B0FHWMCNWK", "foto": "photo-1522041350204-22285237eeca", "categoria": "fuego", "titulo": "Hornillo Camping Gas Portátil con adaptador de bombona + 4 cartuchos", "descripcion": "Hornillo de gas portátil pensado para cocinar en exterior o durante un corte de suministro en casa con ventilación adecuada. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "Humpti", "Dimensiones": "28l. x 11an. x 34,5al. centímetros", "Peso": "1 kg"} },
    {"asin": "B0G45JL8F3", "foto": "photo-1624464313271-4f6f86599d67", "categoria": "fuego", "titulo": "Hornillo Camping Gas Portátil 2 en 1, adaptador para bombona grande o cartucho", "descripcion": "Hornillo de gas portátil pensado para cocinar en exterior o durante un corte de suministro en casa con ventilación adecuada. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "3JG", "Dimensiones": "34l. x 28an. x 12al. centímetros"} },
    {"asin": "B0GZBKB6DD", "foto": "photo-1773762159864-59966f6f82c7", "categoria": "fuego", "titulo": "Cocina de gas portátil de 1 fuego, 2,5 kW, ligera para mochila", "descripcion": "Hornillo de gas portátil pensado para cocinar en exterior o durante un corte de suministro en casa con ventilación adecuada. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "MAXELLPOWER", "Dimensiones": "50l. x 50an. x 50al. centímetros"} },
    {"asin": "B01DBM79MK", "foto": "photo-1505751105760-8f258f2ba88c", "categoria": "fuego", "titulo": "Esbit Pastillas de Combustible Sólido 5g — para cocinar o encender barbacoa", "descripcion": "Pastillas de combustible sólido para cocinar o encender fuego de forma sencilla, sin necesidad de gas ni electricidad. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "Esbit", "Peso": "80 g"} },
    {"asin": "B07NQHP4KS", "foto": "photo-1461484261293-7175bb44e871", "categoria": "fuego", "titulo": "Light My Fire Pedernal de Supervivencia Scout — encendedor de ferrocerio", "descripcion": "Encendedor de emergencia (pedernal o arco eléctrico) pensado como método de encendido de reserva cuando fallan las cerillas o mecheros convencionales. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "Light My Fire", "Peso": "25 g"} },
    {"asin": "B0CNH1DDNC", "foto": "photo-1575908539629-62b3f98d7b3a", "categoria": "fuego", "titulo": "Mechero de Arco Eléctrico USB, recargable, resistente al viento y al agua", "descripcion": "Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "HOSPAOP", "Peso": "230 g", "Dimensiones": "26l. x 1,5an. x 1,5Grosor centímetros"} },
    {"asin": "B0DP4QC3DS", "foto": "photo-1607585475596-9da9238a7d6b", "categoria": "fuego", "titulo": "Fire-Maple G3 Olla Ultraligera de Titanio para camping y supervivencia", "descripcion": "Olla ultraligera de camping, pensada para cocinar con el mínimo peso y volumen posibles. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "Fire-Maple", "Dimensiones": "16f. x 13an. x 13al. centímetros", "Peso": "185 g", "Tamaño": "0.8 Litros"} },
    {"asin": "B0748DJGV9", "foto": "photo-1617118602199-d3c05ae37ed8", "categoria": "fuego", "titulo": "RAPICCA Guantes de Barbacoa Resistentes al Calor hasta 500°C", "descripcion": "Guantes resistentes al calor para manipular ollas, hornillos o brasas con seguridad. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {} },
    {"asin": "B0D2QK85Q8", "foto": "photo-1615801833131-21536b93d516", "categoria": "fuego", "titulo": "Estufa de Alcohol Portátil Mini, plegable y ligera para cocinar en exterior", "descripcion": "Estufa de alcohol ultraligera pensada para cocinar en exterior con un combustible fácil de conseguir y almacenar. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "Foppla", "Peso": "213 g"} },
    {"asin": "B09QGHFLK2", "foto": "photo-1775626094623-99a26d94dc64", "categoria": "fuego", "titulo": "Boundless Voyage Estufa de Alcohol de Titanio Ultraligera para mochileros", "descripcion": "Estufa de alcohol ultraligera pensada para cocinar en exterior con un combustible fácil de conseguir y almacenar. Pensado para cocinar o generar calor de forma segura durante una acampada o una emergencia.", "atributos": {"Marca": "Boundless Voyage", "Dimensiones": "14,4l. x 14,4an. x 8,2al. centímetros", "Peso": "107 g"} },
    {"asin": "B0FSZDG5P4", "foto": "photo-1619164025189-5c01101dfa46", "categoria": "libros", "titulo": "Guía de Preparacionismo y Supervivencia: la información necesaria para prepararte de forma realista", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "B0F8V1T1NR", "foto": "photo-1592355591823-2657dbc25ce0", "categoria": "libros", "titulo": "Manual de Supervivencia Familiar Urbana: Guía 72 Horas para Pisos Urbanos (agua, comida, comunicación)", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "840917748X", "foto": "photo-1507752533523-5186b0bc4c43", "categoria": "libros", "titulo": "Manual de Supervivencia Urbana: Técnicas y Tácticas de Supervivencia Moderna", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "B0GVK5KVJ5", "foto": "photo-1532347833815-3b8e47e7bd7c", "categoria": "libros", "titulo": "Supervivencia Extrema: manual definitivo para sobrevivir a crisis y situaciones límite", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "0062378074", "foto": "photo-1776698540701-983b93156ae2", "categoria": "libros", "titulo": "SAS Survival Handbook (edición en inglés) — el manual de referencia clásico de supervivencia de Lofty Wiseman", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "8428216886", "foto": "photo-1551772413-6c1b7dc18548", "categoria": "libros", "titulo": "Plantas Silvestres Comestibles — Nueva Generación, guía de identificación y recolección", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "8408269356", "foto": "photo-1631551221198-02e14f5c9222", "categoria": "libros", "titulo": "El ABC del Bushcraft: técnicas esenciales de vida en la naturaleza", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "1079712348", "foto": "photo-1577075761882-e89bfab7143e", "categoria": "libros", "titulo": "101 Técnicas y Consejos de Supervivencia para cualquier situación", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "8408304798", "foto": "photo-1764370079194-49403d0411b3", "categoria": "libros", "titulo": "Bushcraft Avanzado: Guía de Nivel Experto para la vida en el bosque", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },
    {"asin": "8408319299", "foto": "photo-1577450775949-58ec8d02cad9", "categoria": "libros", "titulo": "Manual de Supervivencia Urbana: cómo actuar ante cortes de suministro, desabastecimiento y crisis en la ciudad", "descripcion": "Libro o guía de referencia sobre supervivencia, preparacionismo o vida en la naturaleza, pensado para consulta y aprendizaje previo a una emergencia. Una guía de referencia para quienes quieren profundizar en preparacionismo, supervivencia o bushcraft.", "atributos": {} },

    # ENERGÍA
    {"asin": "B01EXWCPLC", "foto": "photo-1621495995068-18144056a287", "categoria": "energia", "titulo": "BigBlue 28W Cargador Solar Portátil con Amperímetro Digital (USB-C/USB-A)", "descripcion": "Panel solar plegable y portátil, pensado para cargar power banks, estaciones de energía o dispositivos pequeños de forma autónoma. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Potencia": "28 vatios", "Marca": "BigBlue", "Peso": "671 g"}},
    {"asin": "B0DQ8PY91X", "foto": "photo-1652326320478-38c1e9842e85", "categoria": "energia", "titulo": "BigBlue 60W Panel Solar Plegable ETFE con QC3.0+PD45W+Salida de CC de 22,2V", "descripcion": "Panel solar plegable y portátil, pensado para cargar power banks, estaciones de energía o dispositivos pequeños de forma autónoma. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Potencia": "60 vatios", "Marca": "BigBlue", "Peso": "2,54 kg"}},
    {"asin": "B095Y957G4", "foto": "photo-1680050973254-450bf851e2a1", "categoria": "energia", "titulo": "BigBlue 100W Panel Solar Portátil N-Type con USB-C PD45W/ USB-A 18W/ MC -4", "descripcion": "Panel solar plegable y portátil, pensado para cargar power banks, estaciones de energía o dispositivos pequeños de forma autónoma. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Potencia": "100 Vatios", "Dimensiones": "55,3l. x 3,5an. x 53,1al. centímetros", "Peso": "2,93 kg", "Marca": "BigBlue"}},
    {"asin": "B0G641B35K", "foto": "photo-1650785652040-5a2fc88ce902", "categoria": "energia", "titulo": "Dyness Estación de Energía Portátil 300W, 256Wh Generador Solar Portatil con Batería LiFeP", "descripcion": "Estación de energía portátil (generador solar) con batería recargable, pensada para alimentar electrodomésticos y dispositivos durante un corte de suministro. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Capacidad": "256 Wh", "Dimensiones": "23l. x 12an. x 17al. centímetros", "Marca": "Dyness"}},
    {"asin": "B0D9TVGW51", "foto": "photo-1678775882799-2fba7042e7da", "categoria": "energia", "titulo": "Batería de reserva portátil recargable de 1000 W/666 Wh, para camping, caravanas, drones,", "descripcion": "Estación de energía portátil (generador solar) con batería recargable, pensada para alimentar electrodomésticos y dispositivos durante un corte de suministro. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Potencia": "1000 Vatios", "Peso": "7,65 kg", "Dimensiones": "26l. x 19an. x 20al. centímetros"}},
    {"asin": "B0GJC2M84T", "foto": "photo-1678775882496-59554c53e32e", "categoria": "energia", "titulo": "Estación de energía portátil DJI Power 1000 Mini, Batería LFP de 1008 WH", "descripcion": "Estación de energía portátil (generador solar) con batería recargable, pensada para alimentar electrodomésticos y dispositivos durante un corte de suministro. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Peso": "11,5 kg", "Dimensiones": "31,4l. x 21,2an. x 21,6Grosor centímetros", "Marca": "DJI"}},
    {"asin": "B0CTH7L29Z", "foto": "photo-1585995603413-eb35b5f4a50b", "categoria": "energia", "titulo": "JUOVI Power Bank 45W 20000mAh Cargador Portátil", "descripcion": "Batería externa (power bank) de gran capacidad, pensada para recargar el teléfono y otros dispositivos varias veces sin acceso a la red eléctrica. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Capacidad": "20000 mAh", "Peso": "373 g", "Dimensiones": "13,7l. x 7an. x 2,6Grosor centímetros"}},
    {"asin": "B0DCBB2YTR", "foto": "photo-1614399113305-a127bb2ca893", "categoria": "energia", "titulo": "Anker Zolo Power Bank 25.000mAh 165W con Tres Puertos USB C", "descripcion": "Batería externa (power bank) de gran capacidad, pensada para recargar el teléfono y otros dispositivos varias veces sin acceso a la red eléctrica. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Capacidad": "25000 mAh", "Peso": "300 g", "Dimensiones": "15,7l. x 5,4an. x 4,9Grosor centímetros", "Marca": "Anker"}},
    {"asin": "B0DCB6FZ46", "foto": "photo-1706275399494-fb26bbc5da63", "categoria": "energia", "titulo": "Power Bank 50000mAh con Cable Incorporado: Batería Externa de Carga rápida de 22.5W con Gr", "descripcion": "Batería externa (power bank) de gran capacidad, pensada para recargar el teléfono y otros dispositivos varias veces sin acceso a la red eléctrica. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {"Marca": "Powelephant", "Peso": "800 g", "Dimensiones": "7l. x 7an. x 15Grosor centímetros"}},
    {"asin": "B0CBZ6ZTMQ", "foto": "photo-1594843665794-446ce915d840", "categoria": "energia", "titulo": "Power Bank 100000 mAh cargador portátil batería externa con pantalla digital LCD 3 entrada", "descripcion": "Batería externa (power bank) de gran capacidad, pensada para recargar el teléfono y otros dispositivos varias veces sin acceso a la red eléctrica. Pensado para generar, almacenar o transportar energía eléctrica de forma autónoma durante cortes de suministro, viajes o acampada.", "atributos": {}},
]


def amazon_link(asin):
    return f"https://www.amazon.es/dp/{asin}?tag={AFFILIATE_TAG}&linkCode=ogi&th=1&psc=1"


def product_card(p):
    cat = next(c for c in CATEGORIES if c["id"] == p["categoria"])
    return f"""        <article class="tarjeta-producto">
          <a class="tarjeta-enlace-ficha" href="../ficha.html?asin={p['asin']}" aria-label="Ver ficha de {p['titulo']}">
            <div class="tarjeta-img tarjeta-foto"><img src="https://images.unsplash.com/{p['foto']}?w=400&h=400&fit=crop&auto=format&q=70" alt="Imagen ilustrativa: {p['titulo']}" loading="lazy"><span class="foto-ilustrativa">Imagen ilustrativa</span></div>
            <div class="tarjeta-cuerpo-superior">
              <span class="tarjeta-cat">{cat['icono']} {cat['nombre']}</span>
              <h3 class="tarjeta-titulo">{p['titulo']}</h3>
            </div>
          </a>
          <div class="tarjeta-cuerpo-inferior">
            <div class="tarjeta-acciones">
              <button type="button" class="add-carrito-btn" data-asin="{p['asin']}">+ Carrito</button>
              <a class="tarjeta-btn" href="{amazon_link(p['asin'])}" target="_blank" rel="nofollow sponsored noopener">Ver precio en Amazon →</a>
            </div>
          </div>
        </article>"""


def category_nav():
    items = "\n".join(f'          <li><a href="{c["id"]}.html">{c["icono"]} {c["nombre"]}</a></li>' for c in CATEGORIES)
    return items


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo_seo} — PrepForCaos</title>
<meta name="description" content="{meta}">
<meta property="og:site_name" content="PrepForCaos">
<meta property="og:type" content="website">
<meta property="og:url" content="https://prepforcaos.com/paginas/{id}.html">
<meta property="og:title" content="{titulo_seo} — PrepForCaos | Equípate para el fin del mundo">
<meta property="og:description" content="{meta}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{titulo_seo} — PrepForCaos">
<meta name="twitter:description" content="{meta}">
<link rel="canonical" href="https://prepforcaos.com/paginas/{id}.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>

<div class="aviso-afiliacion">
  Como Afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables. <a href="afiliacion.html">Más info</a>
</div>

<header class="site-header">
  <div class="header-inner">
    <a href="../index.html" class="logo">
      <span class="icono">🎒</span>
      <span>PREPFORCAOS<span class="sub">Preparacionismo &amp; Supervivencia</span></span>
    </a>
    <nav class="header-nav">
      <a href="../index.html#catalogo">Catálogo completo</a>
      <a href="afiliacion.html">Aviso de afiliación</a>
    </nav>
    <button type="button" class="carrito-abrir carrito-btn-header" aria-label="Abrir carrito de compra">
      <span aria-hidden="true">🛒</span>
      <span class="carrito-badge" hidden>0</span>
    </button>
  </div>
</header>

<section class="hero" style="padding:38px 20px 30px;">
  <div class="contenedor">
    <p style="color:var(--arena-osc); font-size:13px; margin-bottom:10px;"><a href="../index.html" style="color:var(--arena-osc);">Inicio</a> / {nombre}</p>
    <span class="slogan">Equípate para el fin del mundo</span>
    <h1 style="font-size:clamp(24px,4vw,34px);">{icono} {nombre}</h1>
    <p style="max-width:680px; margin:14px auto 0;">{intro}</p>
  </div>
</section>

<section class="productos-sección contenedor" style="padding-top:34px;">
  <div class="truco-caja">
    <h3>{icono} El truco del prepper: {nombre}</h3>
    <ul>
{consejos_html}
    </ul>
  </div>

  <div class="grid-productos">
{productos_html}
  </div>

  <p style="text-align:center; margin-top:34px;">
    <a href="../index.html#catalogo" class="btn btn-outline" style="color:var(--verde-oliva); border-color:var(--verde-oliva);">← Ver el catálogo completo de PrepForCaos</a>
  </p>
</section>

<footer class="site-footer">
  <div class="contenedor">
    <div class="footer-grid">
      <div>
        <h4>PREPFORCAOS</h4>
        <p class="tagline">Equípate para el fin del mundo</p>
        <p style="max-width:340px; color:var(--arena-osc);">Catálogo independiente de equipo de preparacionismo y supervivencia. No somos Amazon ni estamos afiliados a las marcas mostradas; enlazamos a sus fichas de producto en Amazon.es.</p>
      </div>
      <div>
        <h4>Categorías</h4>
        <ul>
{categorias_nav}
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="afiliacion.html">Aviso de afiliación</a></li>
          <li><a href="privacidad.html">Política de privacidad</a></li>
          <li><a href="cookies.html">Política de cookies</a></li>
          <li><a href="aviso-legal.html">Aviso legal</a></li>
        </ul>
      </div>
    </div>
    <p class="footer-disclosure">
      PrepForCaos es un sitio participante en el Programa de Afiliados de Amazon EU, un programa de publicidad para afiliados diseñado para ofrecer a los sitios web un modo de obtener comisiones por publicidad, publicitando e incluyendo enlaces a Amazon.es. Como Afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables. Consulta el precio y la disponibilidad actualizados directamente en Amazon.es.
    </p>
    <p class="footer-bottom">© <span id="anio"></span> PrepForCaos — prepforcaos.com</p>
  </div>
</footer>

<div id="carrito-overlay" class="carrito-overlay"></div>
<aside id="carrito-panel" class="carrito-panel" aria-label="Carrito de compra">
  <div class="carrito-panel-header">
    <h3>🛒 Tu carrito</h3>
    <button type="button" class="carrito-cerrar" aria-label="Cerrar carrito">✕</button>
  </div>
  <p id="carrito-vacio" class="carrito-vacio">Tu carrito está vacío. Añade productos desde el catálogo.</p>
  <div id="carrito-lista" class="carrito-lista"></div>
  <div class="carrito-panel-footer">
    <p id="carrito-total" class="carrito-total"></p>
    <a id="carrito-checkout" class="btn" href="#" target="_blank" rel="nofollow sponsored noopener" aria-disabled="true">Finalizar compra en Amazon →</a>
    <button type="button" id="carrito-vaciar" class="carrito-vaciar-btn">Vaciar carrito</button>
    <p class="carrito-nota">Se abrirá Amazon.es con estos productos añadidos a tu carrito. El pago, el envío y las devoluciones se gestionan siempre en Amazon, con todas sus garantías.</p>
  </div>
</aside>

<script src="../js/products.js"></script>
<script src="../js/cart.js"></script>
<script>document.getElementById("anio").textContent = new Date().getFullYear();</script>
</body>
</html>
"""

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "paginas")
    os.makedirs(out_dir, exist_ok=True)
    nav_html = category_nav()

    for cat in CATEGORIES:
        consejos = TIPS[cat["id"]]
        consejos_html = "\n".join(f"      <li>{c}</li>" for c in consejos)
        productos_cat = [p for p in PRODUCTS if p["categoria"] == cat["id"]]
        productos_html = "\n\n".join(product_card(p) for p in productos_cat)

        html = PAGE_TEMPLATE.format(
            titulo_seo=cat["nombre"],
            meta=cat["meta"],
            id=cat["id"],
            icono=cat["icono"],
            nombre=cat["nombre"],
            intro=cat["intro"],
            consejos_html=consejos_html,
            productos_html=productos_html,
            categorias_nav=nav_html,
        )
        out_path = os.path.join(out_dir, f"{cat['id']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Generado:", out_path)


if __name__ == "__main__":
    main()
