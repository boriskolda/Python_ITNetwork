from clovek_tridy import Clovek

karel = Clovek()
karel.jmeno = "Karel Novák"
karel.vek = 33

cyril = Clovek()
cyril.jmeno = "Cyril Nový"
cyril.vek = 27

karel.kamarad = cyril
cyril.kamarad = karel

karel.predstav_se()
cyril.predstav_se()