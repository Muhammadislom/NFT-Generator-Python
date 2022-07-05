from ast import For
from PIL import Image
import os
import random
import threading
import time
import asyncio
x = 0
def arrayAppendLink(linkArray, arrayLink):
	for root, dirs, files in os.walk(linkArray):
		for file in files:
			arrayLink.append(os.path.join(root,file))



# BGPath ="C:/Users/Muhammadislom/Desktop/nft/bg/"

# step 1
# final1Path ="C:/Users/Muhammadislom/Desktop/nft/final1/"
# sharfPath ="C:/Users/Muhammadislom/Desktop/nft/шарф/"
# step 2
# final2Path ="C:/Users/Muhammadislom/Desktop/nft/final2"
# GalavaPath ="C:/Users/Muhammadislom/Desktop/nft/головаСУхом"
# step 3
# final3Path ="C:/Users/Muhammadislom/Desktop/nft/final3"
# rotPath ="C:/Users/Muhammadislom/Desktop/nft/Улыбка"
# usiPath ="C:/Users/Muhammadislom/Desktop/nft/Усы"
# sergiPath ="C:/Users/Muhammadislom/Desktop/nft/ПравыеСерьги"
# step 4
final4Path ="C:/Users/Muhammadislom/Desktop/nft/final4"
glazaPath ="C:/Users/Muhammadislom/Desktop/nft/глаза/"


# levayaNogaPath = "C:/Users/Muhammadislom/Desktop/nft/леваяНога/"
# PravayaNogaPath = "C:/Users/Muhammadislom/Desktop/nft/праваяНога/"
# levayaRukaPath = "C:/Users/Muhammadislom/Desktop/nft/леваяРука/"
# PravayaRukaPath = "C:/Users/Muhammadislom/Desktop/nft/праваяРука/"
# jivotPath = "C:/Users/Muhammadislom/Desktop/nft/живот/"
# RemenPath = "C:/Users/Muhammadislom/Desktop/nft/ремень/"
bgArray = []

# step 1
# final1fArray = []
# sharfArray = []
# step 2
# final2Array = []
# GalavaArray = []
# step 3
# final3Array = []
# rotArray = []
# usiArray = []
# sergiArray = []
# step 4
final4Array = []
glazaArray = []


# LevayaNogaArray = []
# PravayaNogaArray = []
# LevayaRukaArray = []
# PravayaRukaArray = []
# jivotArray = []
# RemenArray = []
# arrayAppendLink(levayaNogaPath,LevayaNogaArray)
# arrayAppendLink(PravayaNogaPath,PravayaNogaArray)
# arrayAppendLink(levayaRukaPath,LevayaRukaArray)
# arrayAppendLink(PravayaRukaPath,PravayaRukaArray)
# arrayAppendLink(jivotPath,jivotArray)
# arrayAppendLink(RemenPath,RemenArray)

# arrayAppendLink(BGPath,bgArray)
# step 1
# arrayAppendLink(sharfPath,sharfArray)
# arrayAppendLink(final1Path,final1fArray)
# step 2
# arrayAppendLink(final2Path,final2Array)
# arrayAppendLink(GalavaPath,GalavaArray)
# step 3
# arrayAppendLink(final3Path,final3Array)
# arrayAppendLink(sergiPath,sergiArray)
# arrayAppendLink(usiPath,usiArray)
# arrayAppendLink(rotPath,rotArray)
# step 4
arrayAppendLink(final4Path,final4Array)
arrayAppendLink(glazaPath,glazaArray)
x = 0
# step 1
# for sharfArrayFor in sharfArray:
# 	sharfArrayFor = Image.open(sharfArrayFor)
# 	for final1fArrayFor in final1fArray:
# 		final1fArrayFor = Image.open(final1fArrayFor)
# 		# final1fArrayFor.save("C:/Users/Muhammadislom/Desktop/nft/final2/" + str(x) + ".png")
# 		# x = x + 1
# 		final1fArrayFor.paste(sharfArrayFor, (0,0), sharfArrayFor)
# 		final1fArrayFor.save("C:/Users/Muhammadislom/Desktop/nft/final2/" + str(x) + ".png")
# 		x = x + 1

# step 2
# for FinalFor in final2Array:
# 	FinalFor = Image.open(FinalFor)
# 	for	GalavaArraFor in GalavaArray:
# 		GalavaArraFor = Image.open(GalavaArraFor)
# 		FinalFor.paste(GalavaArraFor, (0,0),  GalavaArraFor)
# 		FinalFor.save("C:/Users/Muhammadislom/Desktop/nft/final3/" + str(x) + ".png")
# 		x = x + 1
# step 3

# for rotFor in rotArray:
# 	rotFor = Image.open(rotFor)
# 	for sergiFor in sergiArray:
# 		sergiFor = Image.open(sergiFor)
# 		rotFor.paste(sergiFor, (0,0), sergiFor)
# 		for final3For in final3Array:
# 			final3For = Image.open(final3For)
# 			final3For.paste(rotFor, (0,0), rotFor)
# 			# rotFor.paste(final3For, (0,0), final3For)
# 			final3For.save("C:/Users/Muhammadislom/Desktop/nft/final4/" + str(x) + ".png")
# 			x = x + 1
# step 4
# for glazaFor in glazaArray:
# 	glazaFor = Image.open(glazaFor)
# 	for final4For in final4Array:
# 		final4For = Image.open(final4For)
# 		final4For.paste(glazaFor, (0,0), glazaFor)
# 		final4For.save("C:/Users/Muhammadislom/Desktop/nft/final5/" + str(x) + ".png")
# 		x = x + 1

# for LevayaNogafor in LevayaNogaArray:
# 	indexLevayaNogafor = LevayaNogaArray.index(LevayaNogafor)
# 	LevayaNogafor = Image.open(LevayaNogafor)
# 	for levayaRukaFor in LevayaRukaArray:
# 		indexlevayaRukaFor = LevayaRukaArray.index(levayaRukaFor)
# 		levayaRukaFor = Image.open(levayaRukaFor)
# 		levayaRukaFor.paste(LevayaNogafor, (0,0),  LevayaNogafor)
# 		for jivot in jivotArray:
# 			jivot = Image.open(jivot)
# 			levayaRukaFor.paste(jivot, (0,0),  jivot)
# 			for PravayaNogaFor in PravayaNogaArray:
# 				if indexLevayaNogafor == PravayaNogaArray.index(PravayaNogaFor):
# 					PravayaNogaFor = Image.open(PravayaNogaFor)
# 					levayaRukaFor.paste(PravayaNogaFor, (0,0),  PravayaNogaFor)
# 					for RemenFor in RemenArray:
# 						RemenFor = Image.open(RemenFor)
# 						levayaRukaFor.paste(RemenFor, (0,0),  RemenFor)
# 						for PravayaRukaFor in PravayaRukaArray:
# 							if indexlevayaRukaFor == PravayaRukaArray.index(PravayaRukaFor):
# 								PravayaRukaFor = Image.open(PravayaRukaFor)
# 								levayaRukaFor.paste(PravayaRukaFor, (0,0),  PravayaRukaFor)
# 								levayaRukaFor.save("C:/Users/Muhammadislom/Desktop/nft/final/" + str(x) + ".png")
# 								x = x + 1