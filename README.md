# 📈 Cuadro de mandos personal 📊
 
> Usa este repositorio para crear un cuadro de mandos personal con Streamlit. Documenta los siguientes apartados del README.
> Incluye en tu README la url de donde has publicado tu aplicación. Pon la `url` también en el `About` de tu repositorio.

## Objetivo
Diseño de un cuadro de mandos personal para visualización e interacción con un conjunto de datos.

## Los datos
Elige un conjunto de datos que te interese: educación, deportes, trabajo, música, econocomía, etc. 

## Búsqueda de los datos
Busca una fuente para tus datos. Puedes usar una API de un portal de datos abiertos, un conjunto ya publicado, recopilar personalmente datos por scraping, etc.

He utilizado el portal de datos abiertos de Aragón.

## Documentación de los datos
Documenta los datos que vas a usar y su origen. De dónde los has sacado, fuentes, etc. Describe los campos, los valores, las unidades, etc.

He utilizado un csv, donde he extraido datos sobre los conciertos d emúsica clásica y populares en Aragón y en España, desde el 2003 hasta el 2020.

El origen de los datos vienen del portal de datos abiertos del GObierno de Aragón.

Los distintos campos son: Territorio, Año, Música clasica (conciertos), espectadores de música clasica, recaudación de música clásica, espectadores por representación y gasto medio por espectador y lo mismo con la música clásica pero con la música popular.

## Prepara tu aplicación.
La aplicación se llamará `app.py`. Añade un `requirements.txt` con las dependencias de tu aplicación. Ve actualizándolo a medida que vayas añadiendo librerías.

He añadido: altair, numpy y plotly

## Carga y análisis de conjunto de dato con pandas
Carga el conjunto de datos en un dataframe de pandas y realiza un análisis exploratorio de los datos.

## Visualización de los datos
Prepara visualizaciones diferentes del dataframe en texto (tablas) o gráficas (histogramas, barras, etc.). Puedes usar matplotlib, seaborn, plotly, etc.

He realizado visualizaciones como una tabla general de todo, tabal sobre la música clásica en Aragón, suma de recaudación de clásica en España, 
Gráfica sobre el gasto medio por espectador en conciertos de música clasica en comparación con la popular, un rango sobre espectadores, 
otro sobre el año que quieres ver el concierto, otro sobre el lugar del evento, un radio button sobre el lugar de eventos 
y Gráfica sobre la recaudación en miles de euros, comparando los conciertos de música clásica con los de música popular.

## Diseña la interacción que van a tener tus datos
Qué inputs y outputs tendrán tus datos. 

## Prepara la aplicación (cuadro de mandos) con Streamlit
Prepara y prueba la aplicación.

Para poder arrancar al aplicacion, hayq ue ejcutar el comando streamlit run app.py

## Publica la aplicación.
Publica la aplicación en Streamlit Cloud, en Heroku o en el servicio que prefieras https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app
