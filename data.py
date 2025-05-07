import yaml


def loadSettingsYAML(File):
    class Settings: pass
    with open(File) as f:
        docs = yaml.load_all(f, Loader = yaml.FullLoader)
        for doc in docs:
            for k, v in doc.items():
                setattr(Settings, k, v)
        return Settings

Settings = loadSettingsYAML("Settings.yaml")

obs=[
    #Lavadero
    [
        [ #Pared derecha
            [100,0,0],
            [100,Settings.DimY,0],
            [100,Settings.DimY,237],
            [100,0,237]
        ],
        [ #Pared inferior
            [0,0,237],
            [0,Settings.DimY,237],
            [100,Settings.DimY,237],
            [100,0,237]
        ]
    ],
    #Zona apartada
    [
        [ #Pared derecha
            [200,0,0],
            [200,Settings.DimY,0],
            [200,Settings.DimY,237],
            [200,0,237]
        ],
        [ #Pared inferior
            [100,0,237],
            [100,Settings.DimY,237],
            [200,Settings.DimY,237],
            [200,0,237]
        ]
    ],
    #Columna superior
    [
        [ #Pared derecha
            [Settings.DimX-383,0,0],
            [Settings.DimX-383,Settings.DimY,0],
            [Settings.DimX-383,Settings.DimY,int(7.5)],
            [Settings.DimX-383,0,int(7.5)]
        ],
        [ #Pared inferior
            [Settings.DimX-383,0,int(7.5)],
            [Settings.DimX-383,Settings.DimY,int(7.5)],
            [Settings.DimX-383-int(34.5),Settings.DimY,int(7.5)],
            [Settings.DimX-383-int(34.5),0,int(7.5)]
        ],
        [ #Pared izquierda
            [Settings.DimX-383-int(34.5),0,0],
            [Settings.DimX-383-int(34.5),Settings.DimY,0],
            [Settings.DimX-383-int(34.5),Settings.DimY,int(7.5)],
            [Settings.DimX-383-int(34.5),0,int(7.5)]
        ]
    ],
    #Columna inferior
    [
        [ #Pared izquierda
            [Settings.DimX-383-36,0,404],
            [Settings.DimX-383-36,Settings.DimY,404],
            [Settings.DimX-383-36,Settings.DimY,404+33],
            [Settings.DimX-383-36,0,404+33]
        ],
        [ #Pared inferior
            [Settings.DimX-383,0,404+33],
            [Settings.DimX-383,Settings.DimY,404+33],
            [Settings.DimX-383-36,Settings.DimY,404+33],
            [Settings.DimX-383-36,0,404+33]
        ],
        [ #Pared derecha
            [Settings.DimX-383,0,404],
            [Settings.DimX-383,Settings.DimY,404],
            [Settings.DimX-383,Settings.DimY,404+33],
            [Settings.DimX-383,0,404+33]
        ],
        [ #Pared superior
            [Settings.DimX-383,0,404],
            [Settings.DimX-383,Settings.DimY,404],
            [Settings.DimX-383-36,Settings.DimY,404],
            [Settings.DimX-383-36,0,404+33]
        ],
    ],
    #Puerta principal
    [
        [
            [Settings.DimX-2,0,150],
            [Settings.DimX-2,Settings.DimY,150],
            [Settings.DimX-2,Settings.DimY,150+213],
            [Settings.DimX-2,0,150+213]
        ],
    ],
    #Muro de baño
    [
        [ #Pared izquierda
            [Settings.DimX-720-70,0,337],
            [Settings.DimX-720-70,Settings.DimY,337],
            [Settings.DimX-720-70,Settings.DimY,337+188],
            [Settings.DimX-720-70,0,337+188]
        ],
        [ #Pared inferior
            [0,0,337+188],
            [0,Settings.DimY,337+188],
            [Settings.DimX-720,Settings.DimY,337+188],
            [Settings.DimX-720,0,337+188]
        ],
        [ #Pared derecha
            [Settings.DimX-720,0,337],
            [Settings.DimX-720,Settings.DimY,337],
            [Settings.DimX-720,Settings.DimY,337+188],
            [Settings.DimX-720,0,337+188]
        ],
        [ #Pared superior
            [Settings.DimX-720-70,0, 337],
            [Settings.DimX-720-70,Settings.DimY, 337],
            [Settings.DimX-720,Settings.DimY, 337],
            [Settings.DimX-720,0, 337]
        ],
    ],
    #Muro izquierdo
    [
        [ #Pared inferior
            [0, 0, Settings.DimZ-181],
            [0,Settings.DimY, Settings.DimZ-181],
            [Settings.DimX-720-98,Settings.DimY, Settings.DimZ-181],
            [Settings.DimX-720-98, 0, Settings.DimZ-181]
        ],
        [ #Pared derecha
            [Settings.DimX-720-98,0,337+188],
            [Settings.DimX-720-98,Settings.DimY,337+188],
            [Settings.DimX-720-98,Settings.DimY,Settings.DimZ-181],
            [Settings.DimX-720-98,0,Settings.DimZ-181]
        ],
    ],
    #Muro derecho
    [
        [ #Pared izquierda
            [Settings.DimX-27, 0, 150+213],
            [Settings.DimX-27, Settings.DimY, 150+213],
            [Settings.DimX-27, Settings.DimY,Settings.DimZ-181],
            [Settings.DimX-27, 0,Settings.DimZ-181]
        ],
        [ #Pared inferior
            [Settings.DimX, 0, Settings.DimZ-181],
            [Settings.DimX, Settings.DimY, Settings.DimZ-181],
            [Settings.DimX-27, Settings.DimY, Settings.DimZ-181],
            [Settings.DimX-27, 0, Settings.DimZ-181]
        ],
        [ #Pared superior
            [Settings.DimX, 0, 150+213],
            [Settings.DimX, Settings.DimY, 150+213],
            [Settings.DimX-27, Settings.DimY, 150+213],
            [Settings.DimX-27, 0, 150+213]
        ],
    ],
]

nodos = [
    # [# 1
    #     Settings.DimX,
    #     0,
    #     250
    # ],
    [# 1
        Settings.DimX,
        0,
        280
    ],
    # [# 2
    #     Settings.DimX-170,
    #     0,
    #     250
    # ],
    #  [# 2
    #     Settings.DimX-77,
    #     0,
    #     250
    # ],
     [# 2
        Settings.DimX-77,
        0,
        280
    ],
    # [# 3
    #     Settings.DimX-401,
    #     0,
    #     250
    # ],
    [# 3
        Settings.DimX-401,
        0,
        280
    ],
    # [# 4
    #     Settings.DimX-570,
    #     0,
    #     280
    # ],
    [# 4
        Settings.DimX-670,
        0,
        280
    ],
    [# 5
        Settings.DimX-750,
        0,
        280
    ],
    [# 6
        Settings.DimX-750,
        0,
        120
    ],
    [# 7
        50,
        0,
        280
    ],
    [# 8
        50,
        0,
        430
    ],
    # [# 9
    #     Settings.DimX-170,
    #     0,
    #     600
    # ],
    [# 9
        Settings.DimX-77,
        0,
        600
    ],
    [# 10
        Settings.DimX-401,
        0,
        600
    ],
    # [# 11
    #     Settings.DimX-570,
    #     0,
    #     600
    # ],
    [# 11
        Settings.DimX-670,
        0,
        600
    ],
    [# 12
        Settings.DimX-770,
        0,
        600
    ],
    [# 13
        Settings.DimX-770,
        0,
        800
    ],
]

ady = [
    [0,1,0,0,0,0,0,0,0,0,0,0,0],#1
    [1,0,1,0,0,0,0,0,0,0,0,0,0],#2
    [0,1,0,1,0,0,0,0,0,0,0,0,0],#3
    [0,0,1,0,1,0,0,0,0,0,1,0,0],#4
    [0,0,0,1,0,1,1,0,0,0,0,0,0],#5
    [0,0,0,0,1,0,0,0,0,0,0,0,0],#6
    [0,0,0,0,1,0,0,1,0,0,0,0,0],#7
    [0,0,0,0,0,0,1,0,0,0,0,0,0],#8
    [0,1,0,0,0,0,0,0,0,1,0,0,0],#9
    [0,0,0,0,0,0,0,0,1,0,1,0,0],#10
    [0,0,0,1,0,0,0,0,0,1,0,1,0],#11
    [0,0,0,0,0,0,0,0,0,0,1,0,1],#12
    [0,0,0,0,0,0,0,0,0,0,0,1,0] #13
]