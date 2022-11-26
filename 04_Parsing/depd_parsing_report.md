# Dependency Parsing
## Train, Parse, and Evaluate Using UDPipe Report
The parser correctly parses the syntactic head but incorrectly parses the dependency label in few cases. For example - 
In the sentence  - De allí procedía la familia del escritor vallisoletano Blas Pajarero, cuya casa se encuentra en la Plaza de San Pedro
'encuentra' the dependancy label is parsed as a conjunction instead of a relative clause modifier.
In different sentences the word 'responsable' is sometimes used with syntactic head as noun or adjective and incorrectly parsed dependenct label as adjectival modifier or root instead of open clausal complement or relative clause modifier.
