import matplotlib.pyplot as plt


languages = ['Python', 'Java', 'C++', 'Javascript']

popularity = [90,70,60,80]
plt.bar(languages, popularity, color='skyblue')
plt.title("Language Populatiry")
plt.show()

print ("hello")