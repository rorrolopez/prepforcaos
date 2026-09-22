// Catálogo de productos — PrepForCaos
// Cada producto enlaza a Amazon.es con el tag de afiliado.
const AFFILIATE_TAG = "cuantificanOb-21";

const CATEGORIES = [
  { id: "agua", nombre: "Agua y Potabilización", icono: "💧" },
  { id: "alimentacion", nombre: "Alimentación de Larga Duración", icono: "🥫" },
  { id: "mochilas", nombre: "Mochilas y Kits de Emergencia", icono: "🎒" },
  { id: "botiquin", nombre: "Botiquín y Primeros Auxilios", icono: "⛑️" },
  { id: "herramientas", nombre: "Herramientas y Multiherramientas", icono: "🛠️" },
  { id: "comunicacion", nombre: "Radio y Comunicación", icono: "📻" },
  { id: "refugio", nombre: "Refugio y Abrigo Térmico", icono: "🏕️" },
  { id: "iluminacion", nombre: "Iluminación y Linternas", icono: "🔦" },
  { id: "fuego", nombre: "Fuego y Cocina de Campaña", icono: "🔥" },
  { id: "libros", nombre: "Libros y Guías de Preparacionismo", icono: "📚" },
];

// "El truco del prepper" — consejos prácticos por categoría.
const TIPS = {
  agua: [
    "Calcula un mínimo de 3-4 litros de agua por persona y día (beber, cocinar e higiene básica) al montar tu reserva de emergencia.",
    "Combina un filtro mecánico con pastillas potabilizadoras de reserva: si el filtro se satura o se rompe, necesitas un plan B.",
    "Si vas a abastecer a más de una persona, una botella o bolsa con filtro rinde más que una simple pajita filtrante.",
    "Rota el agua embotellada almacenada cada 6-12 meses y anota la fecha de compra en el envase.",
  ],
  alimentacion: [
    "Aplica el sistema FIFO (\"primero en entrar, primero en salir\"): coloca la comida nueva detrás y consume primero la más antigua.",
    "Calcula un mínimo orientativo de 2.000 kcal por persona y día para tu reserva de emergencia.",
    "Combina alimentos liofilizados (ligeros, larga duración) con conservas y legumbres, más económicas y fáciles de rotar en el día a día.",
    "Prueba las raciones en casa antes de depender de ellas: comprueba que te sientan bien y que sabes prepararlas.",
    "Guarda siempre un abrelatas manual junto a la comida: sin electricidad, muchos abrelatas eléctricos no sirven de nada.",
  ],
  mochilas: [
    "Sigue la regla de las 72 horas: tu mochila de emergencia (BOB) debe darte autonomía real durante al menos tres días.",
    "Distribuye el peso con cuidado: objetos pesados cerca de la espalda y centrados, los más ligeros arriba o en bolsillos exteriores.",
    "Revisa y actualiza el contenido cada 6 meses: caducidad de alimentos y medicinas, cambios de temporada, ropa que ya no talla.",
    "Adapta el kit a tu núcleo familiar real: medicación crónica, niños pequeños o mascotas cambian por completo lo que necesitas llevar.",
    "Pruébate la mochila cargada al menos una vez antes de necesitarla: el peso \"sobre el papel\" y el peso real casi nunca coinciden.",
  ],
  botiquin: [
    "Un botiquín genérico no sustituye tu medicación personal: añade siempre la tuya, con receta y en su envase original.",
    "Revisa las fechas de caducidad cada 6 meses, sobre todo antisépticos, analgésicos y apósitos estériles.",
    "El material no sirve de mucho sin saber usarlo: un curso básico de primeros auxilios (RCP, control de hemorragias) es tan importante como el botiquín en sí.",
    "Guarda una copia de tu cartilla de vacunación y alergias dentro del botiquín, en una funda impermeable.",
    "Las vendas y gasas suelen agotarse primero en una emergencia real: lleva más cantidad de la que crees necesaria.",
  ],
  herramientas: [
    "Una sola multiherramienta de calidad suele rendir más que varias herramientas sueltas de baja calidad.",
    "Aprende a afilar tu navaja o multiherramienta: una hoja desafilada obliga a hacer más fuerza y es más peligrosa que una bien afilada.",
    "Comprueba la normativa local sobre longitud de hoja antes de llevar una navaja o multiherramienta fuera de casa.",
    "Engrasa las articulaciones de forma periódica para que no se agarroten con el uso, la humedad o el paso del tiempo.",
  ],
  comunicacion: [
    "Ten siempre una fuente de energía manual (manivela o solar) como respaldo para cuando fallen las baterías y la red eléctrica.",
    "Apunta de antemano las frecuencias de emergencia y protección civil de tu zona; en plena crisis no es el momento de buscarlas.",
    "En un apagón, la radio analógica AM/FM suele seguir funcionando cuando internet y la red móvil ya han caído.",
    "Lleva pilas de repuesto aunque tu radio sea solar o de manivela: el sol y el movimiento no siempre bastan para cargarla a tiempo.",
  ],
  refugio: [
    "Ten en cuenta la regla de las 3 horas: sin refugio ni protección térmica adecuada, la hipotermia puede aparecer en menos de tres horas en condiciones adversas.",
    "Las mantas térmicas de aluminio son ligerísimas pero pensadas para un uso puntual: si vas a necesitar el equipo varias noches, un saco vivac más resistente aguanta mejor.",
    "Combina capas: algo aislante bajo el cuerpo para no perder calor por el suelo, y manta o saco por encima.",
    "Guarda el refugio en una bolsa impermeable aparte, para que esté siempre seco y accesible cuando lo necesites.",
  ],
  iluminacion: [
    "Lleva siempre dos fuentes de luz independientes: una principal y otra de repuesto, para no depender de una sola batería.",
    "Prioriza linternas recargables por USB, dinamo o solar frente a las de pilas no recargables: reduces tu dependencia de suministro externo.",
    "Guarda las pilas fuera del dispositivo si no vas a usarlo en mucho tiempo, para evitar que se corroan y lo estropeen.",
    "Un frontal (headlamp) libera las manos y suele ser más práctico que una linterna de mano en una emergencia real.",
  ],
  fuego: [
    "Ten siempre dos métodos de encendido distintos (por ejemplo, mechero y yesquero/pedernal) por si uno falla o se moja.",
    "Nunca uses un hornillo de gas en espacios cerrados sin ventilación: existe riesgo real de intoxicación por monóxido de carbono.",
    "Guarda los cartuchos de gas en un lugar fresco, alejados de cualquier fuente de calor directo.",
    "Practica montar y encender tu hornillo en casa, con calma, antes de tener que depender de él de verdad.",
  ],
  libros: [
    "No necesitas leerte una biblioteca entera: empieza por una guía generalista y profundiza después en los temas que más te interesen (agua, primeros auxilios, autosuficiencia...).",
    "Prioriza los manuales con procedimientos claros paso a paso frente a los que solo dan teoría: en una emergencia real necesitas poder consultarlos rápido.",
    "Guarda al menos una guía en papel dentro de tu mochila de emergencia: si falla la electricidad o el móvil, un libro físico sigue funcionando.",
    "Complementa la teoría con práctica real: monta el hornillo, arma el botiquín o prueba el nudo antes de necesitarlo de verdad.",
    "Desconfía de manuales que prometen soluciones milagrosas o técnicas de riesgo sin avisos de seguridad; prioriza autores y editoriales con trayectoria contrastada.",
  ],
};

const PRODUCTS = [
  // AGUA
  { asin: "B0DT99W4MK", categoria: "agua", titulo: "Katadyn BeFree AC 1,0L Black — Filtro de agua para supervivencia y mochileros", precio: "63,73", rating: "4,5", img: "https://m.media-amazon.com/images/I/71wNJ7eumUL._AC_UL320_.jpg" },
  { asin: "B0DMJCF85X", categoria: "agua", titulo: "Pajita Filtrante 1000 L para Camping, Senderismo y Supervivencia", precio: "52,69", rating: "4,4", img: "https://m.media-amazon.com/images/I/71cUAX-G3EL._AC_UL320_.jpg" },
  { asin: "B0H1XQ5TYJ", categoria: "agua", titulo: "Botella con Filtro Purificador de Agua por Prensado Manual", precio: "49,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/81WWzFxw7aL._AC_UL320_.jpg" },
  { asin: "B00GOPHOSQ", categoria: "agua", titulo: "Aquatabs 8,5 mg — 50 Pastillas Potabilizadoras de Agua", precio: "8,84", rating: "4,6", img: "https://m.media-amazon.com/images/I/710WnCNXAdL._AC_UL320_.jpg" },
  { asin: "B0GMXX2G9S", categoria: "agua", titulo: "AWAKING Pastillas Potabilizadoras de Agua, 48 uds — tratamiento hasta 9.600 litros", precio: "14,95", rating: "4,4", img: "https://m.media-amazon.com/images/I/61IMAxDrNtL._AC_UL320_.jpg" },
  { asin: "B0DM8FNFL5", categoria: "agua", titulo: "VEVOR Sistema de Filtración de Agua por Gravedad 8,5L, acero inoxidable, para uso familiar", precio: "89,90", rating: "4,3", img: "https://m.media-amazon.com/images/I/61v7CY-nbmL._AC_UL320_.jpg" },
  { asin: "B08ZYMXLMH", categoria: "agua", titulo: "Membrane Solutions Sistema de Filtro de Agua Portátil por Gravedad, con bolsa de 6L", precio: "39,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/71+BFNpWsFL._AC_UL320_.jpg" },
  { asin: "B0F3D422BK", categoria: "agua", titulo: "Waterflow Filtro de Agua de 3 Fases para Excursionistas y Kit de Supervivencia", precio: "24,97", rating: "4,6", img: "https://m.media-amazon.com/images/I/719oNL-1qCL._AC_UL320_.jpg" },
  { asin: "B0DXQ1QPSL", categoria: "agua", titulo: "HOTUT Mini Filtro de Agua Personal 1500L, pack de 2 unidades portátiles", precio: "15,99", rating: "4,3", img: "https://m.media-amazon.com/images/I/51jsQRfVs7L._AC_UL320_.jpg" },
  { asin: "B0DJVY6JTW", categoria: "agua", titulo: "Botella Plegable 1000ml con Filtro de 0,01µm, hasta 5.000 litros de agua filtrada", precio: "36,99", rating: "3,9", img: "https://m.media-amazon.com/images/I/61YOBRUgonL._AC_UL320_.jpg" },

  // ALIMENTACIÓN
  { asin: "B004JT7F8I", categoria: "alimentacion", titulo: "ReadyWise 120 raciones — Almuerzo y cena, 13 recetas, hasta 25 años de vida útil", precio: "409,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/61PIOLeLcML._AC_UL320_.jpg" },
  { asin: "B08C9JZYPG", categoria: "alimentacion", titulo: "ReadyWise 60 raciones — Desayuno, comida y cena, bolsa Grab & Go liofilizada", precio: "209,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/61Q+VJTn+7L._AC_UL320_.jpg" },
  { asin: "B0GVG47NB5", categoria: "alimentacion", titulo: "Ración de comida de emergencia para supervivencia y protección civil", precio: "97,10", rating: "5,0", img: "https://m.media-amazon.com/images/I/81oFH2uTXGL._AC_UL320_.jpg" },
  { asin: "B0CKJ1G7GD", categoria: "alimentacion", titulo: "MRE-9 Ración de emergencia — 20 años de vida útil, vitaminas extra, 24 x 500 g", precio: "159,00", rating: "4,8", img: "https://m.media-amazon.com/images/I/61FudnICyCL._AC_UL320_.jpg" },
  { asin: "B084L14VKD", categoria: "alimentacion", titulo: "Paquete de ración de 24 horas del ejército militar francés MRE (pack de 3)", precio: "99,00", rating: "5,0", img: "https://m.media-amazon.com/images/I/91LAOp10zCL._AC_UL320_.jpg" },
  { asin: "B071R95ZTV", categoria: "alimentacion", titulo: "Trek'n Eat Leche Entera en Polvo — leche instantánea con 15 años de vida útil", precio: "35,00", rating: "4,8", img: "https://m.media-amazon.com/images/I/71WXG-JGjQL._AC_UL320_.jpg" },
  { asin: "B08D9WVXNG", categoria: "alimentacion", titulo: "Nutrient Survival Leche en Polvo con Vitaminas — suministro de preparación liofilizado", precio: "83,32", rating: "4,6", img: "https://m.media-amazon.com/images/I/71F3kCnH8FL._AC_UL320_.jpg" },
  { asin: "B0917PD1QY", categoria: "alimentacion", titulo: "Kit de Semillas de Huerto Urbano, 12 vegetales — 5.100 semillas ecológicas para autosuficiencia", precio: "11,95", rating: "4,4", img: "https://m.media-amazon.com/images/I/81XsEiXIXSL._AC_UL320_.jpg" },
  { asin: "B0G262DNB9", categoria: "alimentacion", titulo: "Kit de 24 Variedades de Semillas de Huerto y Hierbas Aromáticas, 13.800 semillas", precio: "16,98", rating: "4,6", img: "https://m.media-amazon.com/images/I/81SuT1VXhZL._AC_UL320_.jpg" },
  { asin: "B0DYHFQW4Z", categoria: "alimentacion", titulo: "Galletas de Emergencia de 20 años de vida útil, 6.840 kcal, 12 bolsas, sabor cacahuete", precio: "38,00", rating: "4,6", img: "https://m.media-amazon.com/images/I/71c4yTlRpXL._AC_UL320_.jpg" },

  // MOCHILAS Y KITS
  { asin: "B0F75GGNZT", categoria: "mochilas", titulo: "Kit de Supervivencia Completo 72 Horas — Camping gas, botiquín táctico, radio solar", precio: "219,95", rating: "4,2", img: "https://m.media-amazon.com/images/I/81AT2JRbOgL._AC_UL320_.jpg" },
  { asin: "B0FL1WWR5Q", categoria: "mochilas", titulo: "Gemmac Kit Supervivencia 140 en 1 — Botiquín, radio a pilas, linterna", precio: "34,99", rating: "4,3", img: "https://m.media-amazon.com/images/I/815QM9E8VXL._AC_UL320_.jpg" },
  { asin: "B07GGPH3CZ", categoria: "mochilas", titulo: "ProCase 40L Mochila Táctica Militar MOLLE — para BOB, caza y senderismo", precio: "29,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/81EXesq07VL._AC_UL320_.jpg" },
  { asin: "B08NF9KH46", categoria: "mochilas", titulo: "QT&QY Mochila Militar Táctica 45L MOLLE — Bug Out Bag de 3 días", precio: "42,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/81Q2KEUMLZL._AC_UL320_.jpg" },
  { asin: "B00149O23M", categoria: "mochilas", titulo: "Ready America Mochila de Emergencia — kit preparado para terremotos y desastres", precio: "215,45", rating: "4,7", img: "https://m.media-amazon.com/images/I/816dH3ZwWUL._AC_UL320_.jpg" },
  { asin: "B0F47YJ2KC", categoria: "mochilas", titulo: "ZHIERNA Riñonera Táctica MOLLE para cinturón, complemento para mochila de emergencia", precio: "19,99", rating: "4,7", img: "https://m.media-amazon.com/images/I/71pi12W0ySL._AC_UL320_.jpg" },
  { asin: "B0DCHC34XW", categoria: "mochilas", titulo: "TSPRO Bolsa Táctica MOLLE Dump Pouch plegable para cinturón o mochila", precio: "20,24", rating: "4,6", img: "https://m.media-amazon.com/images/I/81GV0Glx9dL._AC_UL320_.jpg" },
  { asin: "B0BDK85L3T", categoria: "mochilas", titulo: "CAMELBAK Mochila de Hidratación Classic 4L con depósito de 2L", precio: "83,70", rating: "4,4", img: "https://m.media-amazon.com/images/I/91LRImuU89L._AC_UL320_.jpg" },
  { asin: "B09B3HG12T", categoria: "mochilas", titulo: "YUMQUA Bolsa Estanca Impermeable Dry Bag, varias capacidades, para mantener el equipo seco", precio: "15,98", rating: "4,6", img: "https://m.media-amazon.com/images/I/71mUjNCN3BL._AC_UL320_.jpg" },
  { asin: "B07Y2VFPS1", categoria: "mochilas", titulo: "Unigear Bolsa de Agua para Mochila de Hidratación, libre de BPA", precio: "14,99", rating: "4,2", img: "https://m.media-amazon.com/images/I/61MokCzd5hL._AC_UL320_.jpg" },

  // BOTIQUÍN
  { asin: "B09W2WWZGY", categoria: "botiquin", titulo: "Botiquín maletín mediano de primeros auxilios, doble cierre de seguridad", precio: "24,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/71dwo7X4VVL._AC_UL320_.jpg" },
  { asin: "B07R3RMFC4", categoria: "botiquin", titulo: "HONYAO Botiquín de Primeros Auxilios 200 piezas, mini kit de supervivencia", precio: "21,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/81Tf-uIBVyL._AC_UL320_.jpg" },
  { asin: "B0BDGCLB3C", categoria: "botiquin", titulo: "Botiquín maletín grande de primeros auxilios, kit militar para coche y mochila", precio: "30,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/61it6OfO7-L._AC_UL320_.jpg" },
  { asin: "B0DNLPG9CZ", categoria: "botiquin", titulo: "Thulander Pack 2 Torniquetes Tácticos + 2 Vendajes Israelíes para hemorragias", precio: "17,90", rating: "4,5", img: "https://m.media-amazon.com/images/I/81tTW-yZ--L._AC_UL320_.jpg" },
  { asin: "B0F4RBK2W3", categoria: "botiquin", titulo: "NUVEXIA Botiquín de Primeros Auxilios Premium 300 piezas para coche y viaje", precio: "15,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/81nbEsiBs3L._AC_UL320_.jpg" },
  { asin: "B0BWY1JBL9", categoria: "botiquin", titulo: "RHINO RESCUE Kit Individual de Control de Hemorragias IFAK, botiquín militar de trauma", precio: "55,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/81De3b79nTL._AC_UL320_.jpg" },
  { asin: "B0CNXKWNBQ", categoria: "botiquin", titulo: "Vendaje de Trauma de Emergencia Vent Chest Seal, pack de 2 unidades", precio: "9,01", rating: "4,7", img: "https://m.media-amazon.com/images/I/613Fb-9ampL._AC_UL320_.jpg" },
  { asin: "B0CYCRVMW5", categoria: "botiquin", titulo: "Health Press Vendas de Gasa Elástica, pack de 20 rollos", precio: "11,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/81rxhR9xdXL._AC_UL320_.jpg" },
  { asin: "B0B6427ND9", categoria: "botiquin", titulo: "Peha-Haft Venda Elástica Autoadhesiva y Cohesiva para sujeción de gasas", precio: "3,26", rating: "4,0", img: "https://m.media-amazon.com/images/I/71AoVV2juxL._AC_UL320_.jpg" },
  { asin: "B08LJCN9PF", categoria: "botiquin", titulo: "AIESI Collarín Cervical Ajustable en 4 posiciones EasyLock, inmovilización de cuello", precio: "16,50", rating: "4,2", img: "https://m.media-amazon.com/images/I/71RhzzOnQcS._AC_UL320_.jpg" },

  // HERRAMIENTAS
  { asin: "B0777HG5ZB", categoria: "herramientas", titulo: "Leatherman Signal — Multiherramienta de supervivencia", precio: "159,00", rating: "4,8", img: "https://m.media-amazon.com/images/I/61MvMT4r9XL._AC_UL320_.jpg" },
  { asin: "B0CX32Q354", categoria: "herramientas", titulo: "Leatherman Skeletool CX — Acero inoxidable, fabricada en EE.UU.", precio: "118,99", rating: "4,8", img: "https://m.media-amazon.com/images/I/6167S0P6OVL._AC_UL320_.jpg" },
  { asin: "B095LVRVMZ", categoria: "herramientas", titulo: "BIBURY Multiherramienta de alicates y navaja multiusos con bloqueo de seguridad", precio: "36,10", rating: "4,5", img: "https://m.media-amazon.com/images/I/71IVWMhvRNL._AC_UL320_.jpg" },
  { asin: "B0G2RVVKPS", categoria: "herramientas", titulo: "BIBURY Multiherramienta de titanio y acero damasco con navaja de supervivencia", precio: "65,99", rating: "4,5", img: "https://m.media-amazon.com/images/I/81kefjXaphL._AC_UL320_.jpg" },
  { asin: "B09WHFTYH2", categoria: "herramientas", titulo: "Pala Plegable Multifuncional 58 cm, herramienta militar de supervivencia", precio: "17,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/71qSCyiV8aL._AC_UL320_.jpg" },
  { asin: "B0FHX29QR6", categoria: "herramientas", titulo: "KHU Cuchillo Bushcraft de acero D2 con funda Kydex, para caza y supervivencia", precio: "20,35", rating: "4,8", img: "https://m.media-amazon.com/images/I/71aqlUxLxuL._AC_UL320_.jpg" },
  { asin: "B0DGGNWMJ4", categoria: "herramientas", titulo: "Hacha Vikinga artesanal de bushcraft para camping y supervivencia", precio: "42,71", rating: "4,7", img: "https://m.media-amazon.com/images/I/61fmi9-lrlL._AC_UL320_.jpg" },
  { asin: "B000QD1726", categoria: "herramientas", titulo: "BAHCO Serrucho Plegable de baja fricción — sierra de bushcraft y poda", precio: "22,16", rating: "4,8", img: "https://m.media-amazon.com/images/I/61SU1Fx5aLL._AC_UL320_.jpg" },
  { asin: "B0F98Q4BMN", categoria: "herramientas", titulo: "Brotree Paracord 550 de 4mm, 10m, 7 hebras — cuerda de nylon multiusos", precio: "8,99", rating: "4,5", img: "https://m.media-amazon.com/images/I/81kZGWMPtGL._AC_UL320_.jpg" },
  { asin: "B0CG23K1TF", categoria: "herramientas", titulo: "BOMEI PACK 2 Rollos de Cinta Americana 50mm x 50m, reforzada y resistente", precio: "18,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/71Ij+2HocwL._AC_UL320_.jpg" },

  // COMUNICACIÓN
  { asin: "B09KNPHP9W", categoria: "comunicacion", titulo: "Radio Solar de manivela portátil Dynamo AM/FM con linterna LED", precio: "26,99", rating: "4,3", img: "https://m.media-amazon.com/images/I/71nizpYs86L._AC_UL320_.jpg" },
  { asin: "B0GSQJ7KRG", categoria: "comunicacion", titulo: "Radio de Emergencia Portátil AM/FM con solar recargable y dinamo de manivela", precio: "28,99", rating: "4,3", img: "https://m.media-amazon.com/images/I/71muFBhikEL._AC_UL320_.jpg" },
  { asin: "B0F6MQGN4D", categoria: "comunicacion", titulo: "Radio Solar de Emergencia AM/FM con manivela y batería recargable", precio: "42,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/71lMbSgZ4AL._AC_UL320_.jpg" },
  { asin: "B0FNQP8G4W", categoria: "comunicacion", titulo: "Gaswei G1Pro+ Walkie Talkie de Largo Alcance Profesional, resistente IP67", precio: "79,99", rating: "4,7", img: "https://m.media-amazon.com/images/I/71l-JulYbFL._AC_UL320_.jpg" },
  { asin: "B0GT8SG24D", categoria: "comunicacion", titulo: "ADDTOP Cargador Solar Power Bank 20.000 mAh con carga rápida USB-C", precio: "36,99", rating: "4,2", img: "https://m.media-amazon.com/images/I/71Ywu8sLzBL._AC_UL320_.jpg" },
  { asin: "B0H3TGS56C", categoria: "comunicacion", titulo: "Gosknor Silbato de Emergencia de Titanio, para señalización y rescate", precio: "12,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/61wbS7jjMdL._AC_UL320_.jpg" },
  { asin: "B0CQ32DRNT", categoria: "comunicacion", titulo: "RiToEasysports Espejo de Señales de Supervivencia, reflector multifuncional de rescate", precio: "7,46", rating: "5,0", img: "https://m.media-amazon.com/images/I/61VzorEsb-L._AC_UL320_.jpg" },
  { asin: "B0DBM5G2VQ", categoria: "comunicacion", titulo: "McMurdo FastFind 220 — Baliza de rescate personal (PLB) vía satélite, sin suscripción", precio: "279,00", rating: "4,1", img: "https://m.media-amazon.com/images/I/51Ly6A-OblL._AC_UL320_.jpg" },
  { asin: "B0H6JT7V11", categoria: "comunicacion", titulo: "Denver Radio Portátil Recargable, radio solar de emergencia con manivela", precio: "29,95", rating: "5,0", img: "https://m.media-amazon.com/images/I/714S7Hv25DL._AC_UL320_.jpg" },
  { asin: "B0GYZ9R1FQ", categoria: "comunicacion", titulo: "SOLARBABY Radio de Emergencia DAB+/FM con Power Bank de 20.000 mAh integrado", precio: "58,99", rating: "4,5", img: "https://m.media-amazon.com/images/I/71bAXMLWWqL._AC_UL320_.jpg" },

  // REFUGIO
  { asin: "B09GM8XJ3M", categoria: "refugio", titulo: "HONYAO Saco de dormir de emergencia, manta térmica de aluminio", precio: "9,92", rating: "4,4", img: "https://m.media-amazon.com/images/I/71CbAanjyyL._AC_UL320_.jpg" },
  { asin: "B09GMCTMQC", categoria: "refugio", titulo: "HONYAO Saco de dormir de emergencia tipo Bivy para supervivencia", precio: "17,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/71J7Nhdb6AL._AC_UL320_.jpg" },
  { asin: "B0F7KYSVBM", categoria: "refugio", titulo: "Deecam Saco de dormir de emergencia, aislamiento térmico ligero", precio: "19,87", rating: "4,3", img: "https://m.media-amazon.com/images/I/71dHPQgLx7L._AC_UL320_.jpg" },
  { asin: "B0BH48615L", categoria: "refugio", titulo: "LYN Tienda de Campaña Instantánea, impermeable y ligera para emergencia y supervivencia", precio: "25,99", rating: "4,0", img: "https://m.media-amazon.com/images/I/61ewn6uusgL._AC_UL320_.jpg" },
  { asin: "B07WR1V29Y", categoria: "refugio", titulo: "Night Cat Tienda de Campaña para 1-2 Personas, impermeable y de montaje fácil", precio: "59,99", rating: "4,3", img: "https://m.media-amazon.com/images/I/61nWfIjm3vL._AC_UL320_.jpg" },
  { asin: "B0DXVJM334", categoria: "refugio", titulo: "Yuzonc Colchoneta Camping Ultraligera, aislante y compacta para dormir en emergencias", precio: "27,99", rating: "4,2", img: "https://m.media-amazon.com/images/I/71JHn2l3-cL._AC_UL320_.jpg" },
  { asin: "B0CSPBYYJD", categoria: "refugio", titulo: "Toldo de Camping 3x3m Impermeable, protección solar y de lluvia para refugio improvisado", precio: "32,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/614E1QjdUEL._AC_UL320_.jpg" },
  { asin: "B08HH7NY9J", categoria: "refugio", titulo: "AnorTrek Hamaca de Camping con Mosquitero integrado, para refugio en exterior", precio: "25,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/61km7TutlYL._AC_UL320_.jpg" },
  { asin: "B01M19HAEB", categoria: "refugio", titulo: "Bramble Pack de 10 Mantas Térmicas de Emergencia", precio: "14,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/91ytkXPdjsL._AC_UL320_.jpg" },
  { asin: "B0CJT7JW5Z", categoria: "refugio", titulo: "Kit Lona Impermeable 2x3m multiusos, para refugio, cobertizo o protección de equipo", precio: "13,99", rating: "4,0", img: "https://m.media-amazon.com/images/I/71dyuTMlfQL._AC_UL320_.jpg" },

  // ILUMINACIÓN
  { asin: "B08MLBPRCS", categoria: "iluminacion", titulo: "LEKIA Linterna LED de alta potencia recargable por USB, 5 modos", precio: "23,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/61q2CeTtSRL._AC_UL320_.jpg" },
  { asin: "B0CNKN5YSS", categoria: "iluminacion", titulo: "Shadowhawk Linterna LED de alta potencia, recargable, uso táctico", precio: "28,49", rating: "4,3", img: "https://m.media-amazon.com/images/I/81vGbNzD-0L._AC_UL320_.jpg" },
  { asin: "B0DXDTB6Q2", categoria: "iluminacion", titulo: "Linterna LED de alta potencia recargable, batería de 5000 mAh", precio: "15,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/81Mv7VeuWgL._AC_UL320_.jpg" },
  { asin: "B09MS489TF", categoria: "iluminacion", titulo: "POKISEED Linterna Frontal LED Recargable 1500 lúmenes, USB-C 5000 mAh", precio: "35,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/71QDZY31gbL._AC_UL320_.jpg" },
  { asin: "B09KRQRRFL", categoria: "iluminacion", titulo: "Glocusent Lámpara de Camping, 106 LED, 80 horas de autonomía, recargable USB-C", precio: "24,99", rating: "4,5", img: "https://m.media-amazon.com/images/I/6188dv9x2ZL._AC_UL320_.jpg" },
  { asin: "B0DGBRL3H2", categoria: "iluminacion", titulo: "Sterno Velas de Emergencia, hasta 100 horas de combustión continua", precio: "109,08", rating: "4,7", img: "https://m.media-amazon.com/images/I/71a4Ip+SGEL._AC_UL320_.jpg" },
  { asin: "B0197R8882", categoria: "iluminacion", titulo: "Cyalume SnapLight Barra de Luz Química Verde de 12 horas, señalización de emergencia", precio: "31,13", rating: "4,5", img: "https://m.media-amazon.com/images/I/81GWWC2I9LL._AC_UL320_.jpg" },
  { asin: "B0GGY8TTR2", categoria: "iluminacion", titulo: "HENGBIRD Set de 4 Linternas Dinamo, sin pilas, carga manual de emergencia", precio: "11,99", rating: "4,3", img: "https://m.media-amazon.com/images/I/611AC2Z5D-L._AC_UL320_.jpg" },
  { asin: "B0FXMTMGS8", categoria: "iluminacion", titulo: "Baliza de Emergencia V16 Homologada DGT, sustituye a los triángulos", precio: "12,50", rating: "4,3", img: "https://m.media-amazon.com/images/I/71d6LMVXEJL._AC_UL320_.jpg" },
  { asin: "B0F8QFVH8L", categoria: "iluminacion", titulo: "Pack de 5 Velas de Supervivencia, hasta 30 horas de combustión cada una", precio: "11,99", rating: "4,0", img: "https://m.media-amazon.com/images/I/61CaoqiMl4L._AC_UL320_.jpg" },

  // FUEGO Y COCINA
  { asin: "B0FHWMCNWK", categoria: "fuego", titulo: "Hornillo Camping Gas Portátil con adaptador de bombona + 4 cartuchos", precio: "36,95", rating: "4,5", img: "https://m.media-amazon.com/images/I/81DYqiTKtQL._AC_UL320_.jpg" },
  { asin: "B0G45JL8F3", categoria: "fuego", titulo: "Hornillo Camping Gas Portátil 2 en 1, adaptador para bombona grande o cartucho", precio: "21,49", rating: "4,4", img: "https://m.media-amazon.com/images/I/71dGqttMMPL._AC_UL320_.jpg" },
  { asin: "B0GZBKB6DD", categoria: "fuego", titulo: "Cocina de gas portátil de 1 fuego, 2,5 kW, ligera para mochila", precio: "19,95", rating: "4,3", img: "https://m.media-amazon.com/images/I/61w54dYDSwL._AC_UL320_.jpg" },
  { asin: "B01DBM79MK", categoria: "fuego", titulo: "Esbit Pastillas de Combustible Sólido 5g — para cocinar o encender barbacoa", precio: "7,99", rating: "4,4", img: "https://m.media-amazon.com/images/I/71Y27Y3Lr7L._AC_UL320_.jpg" },
  { asin: "B07NQHP4KS", categoria: "fuego", titulo: "Light My Fire Pedernal de Supervivencia Scout — encendedor de ferrocerio", precio: "14,95", rating: "4,6", img: "https://m.media-amazon.com/images/I/91x7VKOArhL._AC_UL320_.jpg" },
  { asin: "B0CNH1DDNC", categoria: "fuego", titulo: "Mechero de Arco Eléctrico USB, recargable, resistente al viento y al agua", precio: "16,99", rating: "4,5", img: "https://m.media-amazon.com/images/I/61cFeDvTmsL._AC_UL320_.jpg" },
  { asin: "B0DP4QC3DS", categoria: "fuego", titulo: "Fire-Maple G3 Olla Ultraligera de Titanio para camping y supervivencia", precio: "27,95", rating: "4,7", img: "https://m.media-amazon.com/images/I/51NHN4L4BXL._AC_UL320_.jpg" },
  { asin: "B0748DJGV9", categoria: "fuego", titulo: "RAPICCA Guantes de Barbacoa Resistentes al Calor hasta 500°C", precio: "39,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/81vClAKxMvL._AC_UL320_.jpg" },
  { asin: "B0D2QK85Q8", categoria: "fuego", titulo: "Estufa de Alcohol Portátil Mini, plegable y ligera para cocinar en exterior", precio: "14,99", rating: "4,6", img: "https://m.media-amazon.com/images/I/61Ek6eDDAvL._AC_UL320_.jpg" },
  { asin: "B09QGHFLK2", categoria: "fuego", titulo: "Boundless Voyage Estufa de Alcohol de Titanio Ultraligera para mochileros", precio: "41,98", rating: "4,5", img: "https://m.media-amazon.com/images/I/61ZdLp9EguL._AC_UL320_.jpg" },

  // LIBROS Y GUÍAS
  { asin: "B0FSZDG5P4", categoria: "libros", titulo: "Guía de Preparacionismo y Supervivencia: la información necesaria para prepararte de forma realista", precio: "20,59", rating: "4,0", img: "https://m.media-amazon.com/images/I/61MBr7nk9YL._AC_UL320_.jpg" },
  { asin: "B0F8V1T1NR", categoria: "libros", titulo: "Manual de Supervivencia Familiar Urbana: Guía 72 Horas para Pisos Urbanos (agua, comida, comunicación)", precio: "14,99", rating: "4,1", img: "https://m.media-amazon.com/images/I/61qAqXiyDWL._AC_UL320_.jpg" },
  { asin: "840917748X", categoria: "libros", titulo: "Manual de Supervivencia Urbana: Técnicas y Tácticas de Supervivencia Moderna", precio: "20,58", rating: "4,4", img: "https://m.media-amazon.com/images/I/61sHRuqHULL._AC_UL320_.jpg" },
  { asin: "B0GVK5KVJ5", categoria: "libros", titulo: "Supervivencia Extrema: manual definitivo para sobrevivir a crisis y situaciones límite", precio: "12,56", rating: "5,0", img: "https://m.media-amazon.com/images/I/71C3b35xcGL._AC_UL320_.jpg" },
  { asin: "0062378074", categoria: "libros", titulo: "SAS Survival Handbook (edición en inglés) — el manual de referencia clásico de supervivencia de Lofty Wiseman", precio: "23,88", rating: "4,8", img: "https://m.media-amazon.com/images/I/71ccpZJ9ZBL._AC_UL320_.jpg" },
  { asin: "8428216886", categoria: "libros", titulo: "Plantas Silvestres Comestibles — Nueva Generación, guía de identificación y recolección", precio: "24,98", rating: "4,4", img: "https://m.media-amazon.com/images/I/71DjFeAIItL._AC_UL320_.jpg" },
  { asin: "8408269356", categoria: "libros", titulo: "El ABC del Bushcraft: técnicas esenciales de vida en la naturaleza", precio: "17,00", rating: "4,5", img: "https://m.media-amazon.com/images/I/617VlxXNOFL._AC_UL320_.jpg" },
  { asin: "1079712348", categoria: "libros", titulo: "101 Técnicas y Consejos de Supervivencia para cualquier situación", precio: "8,26", rating: "4,3", img: "https://m.media-amazon.com/images/I/41ApCUGfqfL._AC_UL320_.jpg" },
  { asin: "8408304798", categoria: "libros", titulo: "Bushcraft Avanzado: Guía de Nivel Experto para la vida en el bosque", precio: "16,10", rating: "4,5", img: "https://m.media-amazon.com/images/I/41FbEhKeqLL._AC_UL320_.jpg" },
  { asin: "8408319299", categoria: "libros", titulo: "Manual de Supervivencia Urbana: cómo actuar ante cortes de suministro, desabastecimiento y crisis en la ciudad", precio: "16,05", rating: "4,9", img: "https://m.media-amazon.com/images/I/813RVVrOmvL._AC_UL320_.jpg" },
];

function amazonLink(asin) {
  return `https://www.amazon.es/dp/${asin}?tag=${AFFILIATE_TAG}&linkCode=ogi&th=1&psc=1`;
}
