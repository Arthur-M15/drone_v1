from adafruit_servokit import ServoKit
import time
import keyboard  # Pour détecter la touche Échap

# Initialiser la carte PCA9685 avec 16 canaux
kit = ServoKit(channels=16)

# Configurer le canal du servo (exemple : canal 0)
servo_channel = 0

# Configurer les limites d'angle (optionnel, dépend de votre servo)
kit.servo[servo_channel].set_pulse_width_range(500, 2500)  # microsecondes

# Boucle pour tester le servo à différents angles
try:
    while True:
        # Vérifier si la touche 'Échap' est pressée
        if keyboard.is_pressed('esc'):  # Échap
            print("Touche Échap détectée. Revenir à la position de départ.")
            kit.servo[servo_channel].angle = 0  # Retour à la position de départ (0°)
            time.sleep(1)  # Laisser un délai avant de quitter
            break  # Quitter la boucle

        print("Position : 0°")
        kit.servo[servo_channel].angle = 0  # Angle minimum
        time.sleep(2)

        print("Position : 90°")
        kit.servo[servo_channel].angle = 90  # Angle moyen
        time.sleep(2)

        print("Position : 170°")
        kit.servo[servo_channel].angle = 170  # Angle maximum
        time.sleep(2)

except KeyboardInterrupt:
    print("Arrêt du programme.")

print("Programme terminé.")

