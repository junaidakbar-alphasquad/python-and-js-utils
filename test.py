code = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
name = [
  "Slate",
  "Gray",
  "Zinc",
  "Neutral",
  "Stone",
  "Red",
  "Orange",
  "Amber",
  "Yellow",
  "Lime",
  "Green",
  "Emerald",
  "Teal",
  "Cyan",
  "Sky",
  "Blue",
  "Indigo",
  "Violet",
  "Purple",
  "Fuchsia",
  "Pink",
  "Rose",
]
colors=[]
for n in name:
    colors.append(n.lower())
for i in colors:
    for j in code:
         print(f'<div class="bg-{i}-{j} size-20 rounded-lg">bg-{i}-{j}</div>')
        
        # print(f"bg-{i}-{j}")
# for k in colors: