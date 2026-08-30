with open("index.html", "r", encoding="utf-8") as f: t = f.read()
og = "<meta property=\"og:type\" content=\"website\">\n<meta property=\"og:title\" content=\"Dmitriy | Fullstack Разработчик\">\n<meta property=\"og:description\" content=\"Создаю сайты, ботов и ИИ-решения.\">\n<meta property=\"og:image\" content=\"https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200\">\n<meta property=\"og:url\" content=\"https://dmitriy719.github.io/portfolio/\">\n<meta name=\"twitter:card\" content=\"summary_large_image\">\n    "
t = t.replace("<meta name=\"description\"", og + "<meta name=\"description\"")
with open("index.html", "w", encoding="utf-8") as f: f.write(t)
print("OG DONE")
