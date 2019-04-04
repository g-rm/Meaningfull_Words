# Meaningfull Words

Você certamente já viu uma nuvem de palavras. Pois bem, esse projeto tem como intuito obter palavras de maior relevância em conjuntos de texto, ao invés das mais frequentes. Isso se dá utilizando o algoritmo tf-idf em conjunto com alguns recursos da biblioteca NLTK.

## Uso

1 - Certifique-se de instalar todas dependências  
2 - Execute jupyter-notebook  
3 - Insira os arquivos .txt em texts/   
4 - Execute jupyter-notebook   
5 - No jupyter, execute nltk.download() -> install stopwords (apenas na primeira vez)   
6 - Substitua <PATH_TO_texts/> pelo caminho até o diretório   
7 - Execute main.py   

## Aplicações  

Este algoritmo foi utilizado para comparar as palavras mais significativas presentes em crônicas de amor (antigas e modernas), assim como sua diversidade léxica. Foram utilizados corpus de 20 crônicas para cada período de tempo. A hipótese inicial era que as crônicas antigas seriam não somente mais românticas como também mais ricas lexicamente.

## Resultados

|Crônicas Antigas|Crônicas Modernas|
|----------|---------|
|<table> <tr><th>Words</th><th>Score</th></tr><tr><td>bêbado</td><td>0.66</td></tr><td>acaba</td><td>0.51</td><tr><td>filha</td><td>0.48</td></tr><tr><td>amante</td><td>0.46</td></tr><tr><td>amor</td><td>0.43</td></tr><tr><td>sopa</td><td>0.37</td></tr><tr><td>dorme</td><td>0.37</td></tr><tr><td>amor acaba</td><td>0.33</td></tr><tr><td>pai</td><td>0.29</td></tr></table>| <table> <tr><th>Words</th><th>Score</th></tr><tr><td>começa</td><td>0.64</td></tr><tr><td>segundo</td><td>0.49</td></tr><tr><td>princesa</td><td>0.48</td></tr><tr><td>amor começa</td><td>0.47</td></tr><tr><td>bom</td><td>0.38</td></tr><tr><td>beber</td><td>0.38</td></tr><tr><td>cantada</td><td>0.33</td></tr><tr><td>chato</td><td>0.28</td></tr><tr><td>escolhas</td><td>0.25</td></tr> </table>

![Alt text](assets/diversity.png?raw=true "Lexical Diversity")  


  
Os resultados foram totalmente contrários a hipótese inicial para esse conjunto de textos analisados. As crônicas modernas não somente foram mais românticas como também apresentaram maior conjunto de palavras distintas expressas. :)
