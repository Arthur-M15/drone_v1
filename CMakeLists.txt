cmake_minimum_required(VERSION 3.10)  # La version 3.10 est souvent utilisée, mais vous pouvez laisser 3.30 si vous en avez besoin.
project(test1a)

# Spécifier la norme C++ utilisée
set(CMAKE_CXX_STANDARD 20)

# Définir le système cible pour la cross-compilation (Linux ARM)
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)

# Définir le compilateur croisé
set(CMAKE_C_COMPILER /usr/bin/arm-linux-gnueabihf-gcc)
set(CMAKE_CXX_COMPILER /usr/bin/arm-linux-gnueabihf-g++)

# Ajouter le fichier source pour la compilation
add_executable(test1a c++_programs/test.cpp)

# Optionnel : Définir l'emplacement des bibliothèques si nécessaire
#set(CMAKE_FIND_ROOT_PATH /path/to/your/arm/sysroot)
