fav_languages = {
    'Jane':['python','ruby'],
    'sarah':['Julia','c']
}
for name, languages in fav_languages.items():
    print(name.title(), " : \n")
    for language in languages:
        print(language.title())