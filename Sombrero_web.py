import streamlit as str

# Configuración de la página web
str.set_page_config(page_title="El Juicio del Sombrero Seleccionador", page_icon="🎩", layout="centered")

# Inyectar CSS personalizado para estética oscura, fuentes elegantes y fijar la firma abajo a la derecha
str.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Georgia&display=swap');
    
    /* Cambiar fuente principal a Georgia */
    .stApp, div[data-baseweb="textarea"], h1, h2, h3, p, button {
        font-family: 'Georgia', serif !important;
    }
    
    /* Estilo para las preguntas */
    .text-pregunta {
        font-size: 1.15rem;
        font-weight: bold;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    /* Firma fija en la esquina inferior derecha */
    .firma-fixed {
        position: fixed;
        bottom: 15px;
        right: 20px;
        font-size: 11px;
        font-style: italic;
        color: #666666;
        z-index: 9999;
        font-family: 'Arial', sans-serif !important;
    }
    </style>
    <div class="firma-fixed">By Diee para Pri ♥</div>
""", unsafe_allow_html=True)

# =====================================================================
# BANCO DE PREGUNTAS Y REPORTES
# =====================================================================
CUESTIONARIO = [
    {
        "pregunta": "EL SACRIFICIO DEL INOCENTE\n\nVeo en tu mente una ambición dorada... pero para alcanzarla, el destino te exige permitir que un inocente cargue con la culpa de un fracaso ajeno. Nadie morirá, pero su nombre quedará manchado en el barro para siempre. ¿Qué me dice tu conciencia?",
        "opciones": [
            {"texto": "Que el fin justifica los medios. El peón cae para que avance el rey.", "casa": "Slytherin"},
            {"texto": "Que la verdad es sagrada. No edificaré mi gloria sobre las cenizas de un inocente.", "casa": "Hufflepuff"},
            {"texto": "Que desafiaré las opciones. Buscaré otra vía, aunque signifique arriesgar mi propio pellejo.", "casa": "Gryffindor"},
            {"texto": "Que es un frío cálculo. Evalúo matemáticamente qué pérdida daña menos al conjunto.", "casa": "Ravenclaw"}
        ]
    },
    {
        "pregunta": "EL LABERINTO DE LA IMPOTENCIA\n\nTe encuentras atrapado en un sistema donde las reglas son corruptas y los de arriba son intocables. Tu fuerza actual es nula para cambiarlos. ¿Qué rincón de tu mente se activa?",
        "opciones": [
            {"texto": "El desprecio silencioso. Me aíslo en mi propio intelecto para proteger mi cordura.", "casa": "Ravenclaw"},
            {"texto": "La astucia paciente. Busco la grieta del sistema para usar su corrupción a mi favor.", "casa": "Slytherin"},
            {"texto": "El deber silencioso. Me enfoco en proteger y sostener a los míos en el día a día.", "casa": "Hufflepuff"},
            {"texto": "La hoguera interna. Prefiero que el sistema me rompa antes que doblegarme ante él.", "casa": "Gryffindor"}
        ]
    },
    {
        "pregunta": "EL ABISMO DEL MIEDO EXISTENCIAL\n\nSi mirara hoy mismo en lo más profundo de tus temores ocultos... ¿cuál es el vacío que te haría temblar de espanto ante un boggart?",
        "opciones": [
            {"texto": "Ser una sombra intrascendente. Pasar por este mundo sin dejar una huella imborrable.", "casa": "Slytherin"},
            {"texto": "Vivir en el autoengaño. Darme cuenta al final de que pasé mi vida en la ignorancia.", "casa": "Ravenclaw"},
            {"texto": "La mirada del cobarde. Saber que tuve la oportunidad de luchar y elegí esconderme.", "casa": "Gryffindor"},
            {"texto": "La más absoluta soledad. Haber logrado mis metas traicionando a quienes me sostuvieron.", "casa": "Hufflepuff"}
        ]
    },
    {
        "pregunta": "EL FILO DE LA TRAICIÓN\n\nAlguien en quien depositaste tu confianza ciega te ha robado y vendido tus secretos para su propio beneficio. El daño está hecho. ¿Cómo ruge tu naturaleza?",
        "opciones": [
            {"texto": "Con fría justicia. Aplico la ley o las consecuencias con rigor, sin espacio a lágrimas.", "casa": "Ravenclaw"},
            {"texto": "Con veneno paciente. Finjo demencia temporalmente y preparo su caída para cuando menos lo espere.", "casa": "Slytherin"},
            {"texto": "Cortando la soga. Destierro a esa persona de mi vida de inmediato; la venganza es un lastre.", "casa": "Gryffindor"},
            {"texto": "Buscando el porqué. Necesito entender qué rompió nuestro lazo antes de cerrar la herida.", "casa": "Hufflepuff"}
        ]
    },
    {
        "pregunta": "EL SECRETO QUE SALVA O DESTRUYE\n\nTienes en tus manos un pergamino con una verdad oculta que destruiría una institución poderosa pero injusta. Revelarlo causará un caos social masivo e inmediato. ¿Qué haces con ese poder?",
        "opciones": [
            {"texto": "Lo lanzo al fuego del público. Que el mundo arda si es necesario para que la verdad purgue la tierra.", "casa": "Gryffindor"},
            {"texto": "Lo guardo bajo llave. El conocimiento es un arma, y el caos descontrolado es irracional.", "casa": "Ravenclaw"},
            {"texto": "Lo utilizo como moneda de cambio. Una palanca silenciosa para asegurar mi posición y la de los míos.", "casa": "Slytherin"},
            {"texto": "Lo entrego con cautela. Busco un canal de confianza para que la transición sea lo menos dolorosa posible.", "casa": "Hufflepuff"}
        ]
    },
    {
        "pregunta": "LA BALANZA DE LA JUSTICIA CRUCIAL\n\nUn líder al que respetas comete un desliz ético menor para proteger los fondos de su comunidad. Un reglamento estricto te obliga a denunciarlo, lo que destruiría su obra. ¿Hacia dónde se inclina tu balanza?",
        "opciones": [
            {"texto": "Hacia el reglamento. Sin normas claras y universales, la sociedad cae en la barbarie.", "casa": "Ravenclaw"},
            {"texto": "Hacia el líder. Protejo a los míos y al orden práctico por encima de un papel escrito.", "casa": "Slytherin"},
            {"texto": "Hacia el honor. Le exijo en privado que lo enmiende, asumiendo juntos la consecuencia.", "casa": "Gryffindor"},
            {"texto": "Hacia el bienestar colectivo. Callo porque el daño de la denuncia supera por mucho al beneficio.", "casa": "Hufflepuff"}
        ]
    },
    {
        "pregunta": "EL ENTORNO Y TU CONTROL\n\nCuando entras a una reunión o espacio social de alta tensión, ¿cuál es el primer mecanismo inconsciente que ejecutas?",
        "opciones": [
            {"texto": "Medir el terreno. Evaluar quién tiene el poder real y cuáles son sus debilidades.", "casa": "Slytherin"},
            {"texto": "Analizar los datos. Escuchar los argumentos técnicos buscando fallas de lógica o contradicciones.", "casa": "Ravenclaw"},
            {"texto": "Sentir la atmósfera. Asegurarme de que haya un ambiente seguro, pacífico y de confianza mutua.", "casa": "Hufflepuff"},
            {"texto": "Marcar presencia. Mostrar firmeza y autonomía para que nadie intente pasarme por encima.", "casa": "Gryffindor"}
        ]
    },
    {
        "pregunta": "EL VALOR DE LA HERENCIA Y EL LEGADO\n\nSi pudieras elegir cómo inscribir tu nombre en los anales de la historia, ¿cuál de estos resúmenes se asemeja más a tu deseo íntimo?",
        "opciones": [
            {"texto": "Como el arquitecto del cambio. Alguien que desafió las reglas y dejó una estructura nueva.", "casa": "Slytherin"},
            {"texto": "Como la mente preclara. Alguien que trajo luz, conocimiento y entendimiento al caos.", "casa": "Ravenclaw"},
            {"texto": "Como el escudo inquebrantable. Un bastión de rectitud que sostuvo a su comunidad en la tormenta.", "casa": "Hufflepuff"},
            {"texto": "Como la chispa indómita. Alguien que inspiró a otros a romper sus propias cadenas.", "casa": "Gryffindor"}
        ]
    },
    {
        "pregunta": "EL CONTROL DE LA VOLUNTAD\n\nImagina que se te concede un artefacto capaz de doblegar sutilmente la voluntad de un rival por una única vez, sin dejar rastro alguno. ¿Cómo reacciona tu instinto?",
        "opciones": [
            {"texto": "Lo guardo celosamente. Lo usaré como un recurso estratégico definitivo cuando mi posición peligre.", "casa": "Slytherin"},
            {"texto": "Lo destruyo o rechazo. Forzar la mente ajena destruye el libre albedrío y pervierte mi propio honor.", "casa": "Gryffindor"},
            {"texto": "Lo estudio. Necesito comprender cómo funciona y qué principios rigen ese nivel de coacción.", "casa": "Ravenclaw"},
            {"texto": "Lo neutralizo de forma segura. Un poder así solo genera desconfianza y rompe el tejido social.", "casa": "Hufflepuff"}
        ]
    },
    {
        "pregunta": "LA LÍNEA ROJA DEFINITIVA\n\nTodos tenemos un límite que, una vez cruzado, no tiene retorno posible. En tus relaciones personales o profesionales, ¿qué es lo único que consideras imperdonable?",
        "opciones": [
            {"texto": "La traición deliberada de un pacto o de la confianza depositada en alguien.", "casa": "Slytherin"},
            {"texto": "La cobardía sistemática de quien prefiere dejar que otros caigan antes que dar la cara.", "casa": "Gryffindor"},
            {"texto": "La malevolencia irracional que busca destruir por el simple placer de hacer daño.", "casa": "Hufflepuff"},
            {"texto": "La hipocresía y la mentira intelectual de quien manipula la verdad por conveniencia.", "casa": "Ravenclaw"}
        ]
    }
]

REPORTE_PSICOLOGICO = {
    "Slytherin": "¡Ah, una mente de plata y esmeralda! Posees una estructura pragmática y un instinto de preservación afilado como un puñal. No te dejas enredar por moralismos abstractos cuando hay objetivos reales que reclamar. Entiendes el mundo como un tablero de ajedrez donde el poder se gestiona o se padece. Tu astucia es tu mayor escudo, pero cuida que tu desapego no te encierre en tus propias mazmorras.",
    "Ravenclaw": "¡Vaya, un intelecto cristalino! Tu mente opera como un mecanismo de relojería, buscando siempre el orden, la lógica y la verdad detrás del caos. Te repugna la mediocridad y el sesgo de las emociones descontroladas. Eres un observador agudo, capaz de desarmar la realidad en piezas, aunque a veces corres el peligro de tratar los dilemas del corazón humano como simples ecuaciones matemáticas.",
    "Gryffindor": "¡Un espíritu indómito y fiero! Te moviliza la fricción, el desafío y la defense de tu propia autonomía. No soportas las cadenas de la sumisión y prefieres el impacto de una verdad incómoda antes que la comodidad de una mentira tibia. Tienes el coraje de los que saltan al vacío, pero recuerda que un verdadero líder también necesita aprender cuándo envainar la espada y trazar un plan de retirada.",
    "Hufflepuff": "¡Raíces profundas y lealtad inquebrantable! Tu psicología se cimienta sobre la resistencia y la cohesión. Comprendes, con una sabiduría antigua, que ningún imperio sobrevive sin cimientos sólidos y pactos sagrados. Eres el pilar que absorbe el impacto en tiempos de crisis, pero ten cautela: tu nobleza no debe convertirse en un felpudo para los que confunden tu paciencia con debilidad."
}

# =====================================================================
# ESTRUCTURA DE CONTROL DE ESTADOS DE STREAMLIT
# =====================================================================
if "paso" not in str.session_state:
    str.session_state.paso = "bienvenida"
    str.session_state.puntajes = {"Gryffindor": 0, "Slytherin": 0, "Ravenclaw": 0, "Hufflepuff": 0}
    str.session_state.indice = 0

# --- PANTALLA 1: BIENVENIDA ---
if str.session_state.paso == "bienvenida":
    str.subheader("¿QUÉ HAY EN LO PROFUNDO DE TU ALMA?")
    
    discurso = (
        "Mmm... inclínate un poco más. Sí, hace mil años que leo los pensamientos de quienes cruzan estas puertas, "
        "y sigo encontrando los mismos rincones oscuros, lasBooth de ambiciones secretas y los miedos que no se atreven "
        "a susurrar a la luz del día.\n\n"
        "No me interesan tus modales, ni tus respuestas ensayadas para agradar al mundo. He venido a buscar "
        "tu verdadera naturaleza; esa que emerge solo cuando la presión es insoportable y las opciones son "
        "completamente grises. Te pondré frente a 10 encrucijadas difíciles, decisiones que definen quién eres "
        "cuando nadie te está mirando.\n\n"
        "No temas a lo que pueda encontrar. Al fin y al cabo, yo solo reflejo lo que tú ya has decidido ser. "
        "Cruza el umbral cuando estés listo."
    )
    str.text_area("", discurso, height=250, disabled=True)
    
    if str.button("ESCUCHAR EL JUICIO", use_container_width=True):
        str.session_state.paso = "preguntas"
        str.rerun()

# --- PANTALLA 2: PREGUNTAS ---
elif str.session_state.paso == "preguntas":
    idx = str.session_state.indice
    total_p = len(CUESTIONARIO)
    
    str.caption(f"EXAMEN DE CONCIENCIA: {idx + 1} DE {total_p}")
    
    str.markdown(f'<div class="text-pregunta">{CUESTIONARIO[idx]["pregunta"]}</div>', unsafe_allow_html=True)
    
    for i, opcion in enumerate(CUESTIONARIO[idx]["opciones"]):
        if str.button(opcion["texto"], key=f"btn_{idx}_{i}", use_container_width=True):
            str.session_state.puntajes[opcion["casa"]] += 1
            
            if str.session_state.indice + 1 < total_p:
                str.session_state.indice += 1
            else:
                str.session_state.paso = "resultado"
            str.rerun()

# --- PANTALLA 3: VEREDICTO FINAL ---
elif str.session_state.paso == "resultado":
    casa_final = max(str.session_state.puntajes, key=str.session_state.puntajes.get)
    resumen = REPORTE_PSICOLOGICO[casa_final]
    
    colores = {"Slytherin": "#1C4D32", "Gryffindor": "#7F0909", "Ravenclaw": "#0E2849", "Hufflepuff": "#7A6500"}
    color = colores[casa_final]
    
    str.caption("EL SOMBRERO HA DECIDIDO...")
    str.markdown(f"<h1 style='text-align: center; color: {color}; font-size: 3rem;'>{casa_final.upper()}</h1>", unsafe_allow_html=True)
    
    texto_final = f"{resumen}\n\n" \
                  f"────────────────────────────────────────\n" \
                  f"Matriz de afinidad de tu alma:\n" \
                  f"• Slytherin: {str.session_state.puntajes['Slytherin']} vaticinios\n" \
                  f"• Ravenclaw: {str.session_state.puntajes['Ravenclaw']} vaticinios\n" \
                  f"• Gryffindor: {str.session_state.puntajes['Gryffindor']} vaticinios\n" \
                  f"• Hufflepuff: {str.session_state.puntajes['Hufflepuff']} vaticinios"
                  
    str.text_area("", texto_final, height=260, disabled=True)
    
    if str.button("REPETIR DIAGNÓSTICO", use_container_width=True):
        str.session_state.paso = "bienvenida"
        str.session_state.puntajes = {"Gryffindor": 0, "Slytherin": 0, "Ravenclaw": 0, "Hufflepuff": 0}
        str.session_state.indice = 0
        str.rerun()