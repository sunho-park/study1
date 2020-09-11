# 이미지들을 Numpy 형식으로 변환하기
import numpy as np
from PIL import Image              # Python Image Library
import glob, os, random 

outfile = "./vggface/3low_kface100.npz" # 저장할 파일 이름

# max_photo = 200 # 사용할 장 수
photo_size = 224 # 이미지 크기

x = []          # 이미지 데이터
y = []          # 레이블 데이터

def main():
    # 디렉터리 읽어 들이기             
    # for i in os.listdir('D:\lowkface100'):
    #     glob_files("D:\lowkface100/"+str(i), i) 

    glob_files("D:\lowkface100/0", 0)         
    glob_files("D:\lowkface100/1", 1)         
    glob_files("D:\lowkface100/2", 2)         
    # glob_files("D:\lowkface100/3", 3)         
    # glob_files("D:\lowkface100/4", 4)         
    # glob_files("D:\lowkface100/5", 5)         
    # glob_files("D:\lowkface100/6", 6)         
    # glob_files("D:\lowkface100/7", 7)         
    # glob_files("D:\lowkface100/8", 8)         
    # glob_files("D:\lowkface100/9", 9)         
    # glob_files("D:\lowkface100/10", 10)         
    # glob_files("D:\lowkface100/11", 11)         
    # glob_files("D:\lowkface100/12", 12)         
    # glob_files("D:\lowkface100/13", 13)         
    # glob_files("D:\lowkface100/14", 14)         
    # glob_files("D:\lowkface100/15", 15)         
    # glob_files("D:\lowkface100/16", 16)         
    # glob_files("D:\lowkface100/17", 17)         
    # glob_files("D:\lowkface100/18", 18)         
    # glob_files("D:\lowkface100/19", 19)         
    # glob_files("D:\lowkface100/20", 20)         
    # glob_files("D:\lowkface100/21", 21)         
    # glob_files("D:\lowkface100/22", 22)         
    # glob_files("D:\lowkface100/23", 23)         
    # glob_files("D:\lowkface100/24", 24)         
    # glob_files("D:\lowkface100/25", 25)         
    # glob_files("D:\lowkface100/26", 26)         
    # glob_files("D:\lowkface100/27", 27)         
    # glob_files("D:\lowkface100/28", 28)         
    # glob_files("D:\lowkface100/29", 29)         
    # glob_files("D:\lowkface100/30", 30)         
    # glob_files("D:\lowkface100/31", 31)         
    # glob_files("D:\lowkface100/32", 32)         
    # glob_files("D:\lowkface100/33", 33)         
    # glob_files("D:\lowkface100/34", 34)         
    # glob_files("D:\lowkface100/35", 35)         
    # glob_files("D:\lowkface100/36", 36)         
    # glob_files("D:\lowkface100/37", 37)         
    # glob_files("D:\lowkface100/38", 38)         
    # glob_files("D:\lowkface100/39", 39)         
    # glob_files("D:\lowkface100/40", 40)         
    # glob_files("D:\lowkface100/41", 41)         
    # glob_files("D:\lowkface100/42", 42)         
    # glob_files("D:\lowkface100/43", 43)         
    # glob_files("D:\lowkface100/44", 44)         
    # glob_files("D:\lowkface100/45", 45)         
    # glob_files("D:\lowkface100/46", 46)         
    # glob_files("D:\lowkface100/47", 47)         
    # glob_files("D:\lowkface100/48", 48)         
    # glob_files("D:\lowkface100/49", 49)         
    # glob_files("D:\lowkface100/50", 50)         
    # glob_files("D:\lowkface100/51", 51)         
    # glob_files("D:\lowkface100/52", 52)         
    # glob_files("D:\lowkface100/53", 53)         
    # glob_files("D:\lowkface100/54", 54)         
    # glob_files("D:\lowkface100/55", 55)         
    # glob_files("D:\lowkface100/56", 56)         
    # glob_files("D:\lowkface100/57", 57)         
    # glob_files("D:\lowkface100/58", 58)         
    # glob_files("D:\lowkface100/59", 59)         
    # glob_files("D:\lowkface100/60", 60)         
    # glob_files("D:\lowkface100/61", 61)         
    # glob_files("D:\lowkface100/62", 62)         
    # glob_files("D:\lowkface100/63", 63)         
    # glob_files("D:\lowkface100/64", 64)         
    # glob_files("D:\lowkface100/65", 65)         
    # glob_files("D:\lowkface100/66", 66)         
    # glob_files("D:\lowkface100/67", 67)         
    # glob_files("D:\lowkface100/68", 68)         
    # glob_files("D:\lowkface100/69", 69)         
    # glob_files("D:\lowkface100/70", 70)         
    # glob_files("D:\lowkface100/71", 71)         
    # glob_files("D:\lowkface100/72", 72)         
    # glob_files("D:\lowkface100/73", 73)         
    # glob_files("D:\lowkface100/74", 74)         
    # glob_files("D:\lowkface100/75", 75)         
    # glob_files("D:\lowkface100/76", 76)         
    # glob_files("D:\lowkface100/77", 77)         
    # glob_files("D:\lowkface100/78", 78)         
    # glob_files("D:\lowkface100/79", 79)         
    # glob_files("D:\lowkface100/80", 80)         
    # glob_files("D:\lowkface100/81", 81)         
    # glob_files("D:\lowkface100/82", 82)         
    # glob_files("D:\lowkface100/83", 83)         
    # glob_files("D:\lowkface100/84", 84)         
    # glob_files("D:\lowkface100/85", 85)         
    # glob_files("D:\lowkface100/86", 86)         
    # glob_files("D:\lowkface100/87", 87)         
    # glob_files("D:\lowkface100/88", 88)         
    # glob_files("D:\lowkface100/89", 89)         
    # glob_files("D:\lowkface100/90", 90)         
    # glob_files("D:\lowkface100/91", 91)         
    # glob_files("D:\lowkface100/92", 92)         
    # glob_files("D:\lowkface100/93", 93)         
    # glob_files("D:\lowkface100/94", 94)         
    # glob_files("D:\lowkface100/95", 95)         
    # glob_files("D:\lowkface100/96", 96)         
    # glob_files("D:\lowkface100/97", 97)         
    # glob_files("D:\lowkface100/98", 98)         
    # glob_files("D:\lowkface100/99", 99)         
    # glob_files("D:\lowkface100/100", 100)         
    # glob_files("D:\lowkface100/101", 101)         
    # glob_files("D:\lowkface100/102", 102)         
    # glob_files("D:\lowkface100/103", 103)         
    # glob_files("D:\lowkface100/104", 104)         
    # glob_files("D:\lowkface100/105", 105)         
    # glob_files("D:\lowkface100/106", 106)         
    # glob_files("D:\lowkface100/107", 107)         
    # glob_files("D:\lowkface100/108", 108)         
    # glob_files("D:\lowkface100/109", 109)         
    # glob_files("D:\lowkface100/110", 110)         
    # glob_files("D:\lowkface100/111", 111)         
    # glob_files("D:\lowkface100/112", 112)         
    # glob_files("D:\lowkface100/113", 113)         
    # glob_files("D:\lowkface100/114", 114)         
    # glob_files("D:\lowkface100/115", 115)         
    # glob_files("D:\lowkface100/116", 116)         
    # glob_files("D:\lowkface100/117", 117)         
    # glob_files("D:\lowkface100/118", 118)         
    # glob_files("D:\lowkface100/119", 119)         
    # glob_files("D:\lowkface100/120", 120)         
    # glob_files("D:\lowkface100/121", 121)         
    # glob_files("D:\lowkface100/122", 122)         
    # glob_files("D:\lowkface100/123", 123)         
    # glob_files("D:\lowkface100/124", 124)         
    # glob_files("D:\lowkface100/125", 125)         
    # glob_files("D:\lowkface100/126", 126)         
    # glob_files("D:\lowkface100/127", 127)         
    # glob_files("D:\lowkface100/128", 128)         
    # glob_files("D:\lowkface100/129", 129)         
    # glob_files("D:\lowkface100/130", 130)         
    # glob_files("D:\lowkface100/131", 131)         
    # glob_files("D:\lowkface100/132", 132)         
    # glob_files("D:\lowkface100/133", 133)         
    # glob_files("D:\lowkface100/134", 134)         
    # glob_files("D:\lowkface100/135", 135)         
    # glob_files("D:\lowkface100/136", 136)         
    # glob_files("D:\lowkface100/137", 137)         
    # glob_files("D:\lowkface100/138", 138)         
    # glob_files("D:\lowkface100/139", 139)         
    # glob_files("D:\lowkface100/140", 140)         
    # glob_files("D:\lowkface100/141", 141)         
    # glob_files("D:\lowkface100/142", 142)         
    # glob_files("D:\lowkface100/143", 143)         
    # glob_files("D:\lowkface100/144", 144)         
    # glob_files("D:\lowkface100/145", 145)         
    # glob_files("D:\lowkface100/146", 146)         
    # glob_files("D:\lowkface100/147", 147)         
    # glob_files("D:\lowkface100/148", 148)         
    # glob_files("D:\lowkface100/149", 149)         
    # glob_files("D:\lowkface100/150", 150)         
    # glob_files("D:\lowkface100/151", 151)         
    # glob_files("D:\lowkface100/152", 152)         
    # glob_files("D:\lowkface100/153", 153)         
    # glob_files("D:\lowkface100/154", 154)         
    # glob_files("D:\lowkface100/155", 155)         
    # glob_files("D:\lowkface100/156", 156)         
    # glob_files("D:\lowkface100/157", 157)         
    # glob_files("D:\lowkface100/158", 158)         
    # glob_files("D:\lowkface100/159", 159)         
    # glob_files("D:\lowkface100/160", 160)         
    # glob_files("D:\lowkface100/161", 161)         
    # glob_files("D:\lowkface100/162", 162)         
    # glob_files("D:\lowkface100/163", 163)         
    # glob_files("D:\lowkface100/164", 164)         
    # glob_files("D:\lowkface100/165", 165)         
    # glob_files("D:\lowkface100/166", 166)         
    # glob_files("D:\lowkface100/167", 167)         
    # glob_files("D:\lowkface100/168", 168)         
    # glob_files("D:\lowkface100/169", 169)         
    # glob_files("D:\lowkface100/170", 170)         
    # glob_files("D:\lowkface100/171", 171)         
    # glob_files("D:\lowkface100/172", 172)         
    # glob_files("D:\lowkface100/173", 173)         
    # glob_files("D:\lowkface100/174", 174)         
    # glob_files("D:\lowkface100/175", 175)         
    # glob_files("D:\lowkface100/176", 176)         
    # glob_files("D:\lowkface100/177", 177)         
    # glob_files("D:\lowkface100/178", 178)         
    # glob_files("D:\lowkface100/179", 179)         
    # glob_files("D:\lowkface100/180", 180)         
    # glob_files("D:\lowkface100/181", 181)         
    # glob_files("D:\lowkface100/182", 182)         
    # glob_files("D:\lowkface100/183", 183)         
    # glob_files("D:\lowkface100/184", 184)         
    # glob_files("D:\lowkface100/185", 185)         
    # glob_files("D:\lowkface100/186", 186)         
    # glob_files("D:\lowkface100/187", 187)         
    # glob_files("D:\lowkface100/188", 188)         
    # glob_files("D:\lowkface100/189", 189)         
    # glob_files("D:\lowkface100/190", 190)         
    # glob_files("D:\lowkface100/191", 191)         
    # glob_files("D:\lowkface100/192", 192)         
    # glob_files("D:\lowkface100/193", 193)         
    # glob_files("D:\lowkface100/194", 194)         
    # glob_files("D:\lowkface100/195", 195)         
    # glob_files("D:\lowkface100/196", 196)         
    # glob_files("D:\lowkface100/197", 197)         
    # glob_files("D:\lowkface100/198", 198)         
    # glob_files("D:\lowkface100/199", 199)         
    # glob_files("D:\lowkface100/200", 200)         
    # glob_files("D:\lowkface100/201", 201)         
    # glob_files("D:\lowkface100/202", 202)         
    # glob_files("D:\lowkface100/203", 203)         
    # glob_files("D:\lowkface100/204", 204)         
    # glob_files("D:\lowkface100/205", 205)         
    # glob_files("D:\lowkface100/206", 206)         
    # glob_files("D:\lowkface100/207", 207)         
    # glob_files("D:\lowkface100/208", 208)         
    # glob_files("D:\lowkface100/209", 209)         
    # glob_files("D:\lowkface100/210", 210)         
    # glob_files("D:\lowkface100/211", 211)         
    # glob_files("D:\lowkface100/212", 212)         
    # glob_files("D:\lowkface100/213", 213)         
    # glob_files("D:\lowkface100/214", 214)         
    # glob_files("D:\lowkface100/215", 215)         
    # glob_files("D:\lowkface100/216", 216)         
    # glob_files("D:\lowkface100/217", 217)         
    # glob_files("D:\lowkface100/218", 218)         
    # glob_files("D:\lowkface100/219", 219)         
    # glob_files("D:\lowkface100/220", 220)         
    # glob_files("D:\lowkface100/221", 221)         
    # glob_files("D:\lowkface100/222", 222)         
    # glob_files("D:\lowkface100/223", 223)         
    # glob_files("D:\lowkface100/224", 224)         
    # glob_files("D:\lowkface100/225", 225)         
    # glob_files("D:\lowkface100/226", 226)         
    # glob_files("D:\lowkface100/227", 227)         
    # glob_files("D:\lowkface100/228", 228)         
    # glob_files("D:\lowkface100/229", 229)         
    # glob_files("D:\lowkface100/230", 230)         
    # glob_files("D:\lowkface100/231", 231)         
    # glob_files("D:\lowkface100/232", 232)         
    # glob_files("D:\lowkface100/233", 233)         
    # glob_files("D:\lowkface100/234", 234)         
    # glob_files("D:\lowkface100/235", 235)         
    # glob_files("D:\lowkface100/236", 236)         
    # glob_files("D:\lowkface100/237", 237)         
    # glob_files("D:\lowkface100/238", 238)         
    # glob_files("D:\lowkface100/239", 239)         
    # glob_files("D:\lowkface100/240", 240)         
    # glob_files("D:\lowkface100/241", 241)         
    # glob_files("D:\lowkface100/242", 242)         
    # glob_files("D:\lowkface100/243", 243)         
    # glob_files("D:\lowkface100/244", 244)         
    # glob_files("D:\lowkface100/245", 245)         
    # glob_files("D:\lowkface100/246", 246)         
    # glob_files("D:\lowkface100/247", 247)         
    # glob_files("D:\lowkface100/248", 248)         
    # glob_files("D:\lowkface100/249", 249)         
    # glob_files("D:\lowkface100/250", 250)         
    # glob_files("D:\lowkface100/251", 251)         
    # glob_files("D:\lowkface100/252", 252)         
    # glob_files("D:\lowkface100/253", 253)         
    # glob_files("D:\lowkface100/254", 254)         
    # glob_files("D:\lowkface100/255", 255)         
    # glob_files("D:\lowkface100/256", 256)         
    # glob_files("D:\lowkface100/257", 257)         
    # glob_files("D:\lowkface100/258", 258)         
    # glob_files("D:\lowkface100/259", 259)         
    # glob_files("D:\lowkface100/260", 260)         
    # glob_files("D:\lowkface100/261", 261)         
    # glob_files("D:\lowkface100/262", 262)         
    # glob_files("D:\lowkface100/263", 263)         
    # glob_files("D:\lowkface100/264", 264)         
    # glob_files("D:\lowkface100/265", 265)         
    # glob_files("D:\lowkface100/266", 266)         
    # glob_files("D:\lowkface100/267", 267)         
    # glob_files("D:\lowkface100/268", 268)         
    # glob_files("D:\lowkface100/269", 269)         
    # glob_files("D:\lowkface100/270", 270)         
    # glob_files("D:\lowkface100/271", 271)         
    # glob_files("D:\lowkface100/272", 272)         
    # glob_files("D:\lowkface100/273", 273)         
    # glob_files("D:\lowkface100/274", 274)         
    # glob_files("D:\lowkface100/275", 275)         
    # glob_files("D:\lowkface100/276", 276)         
    # glob_files("D:\lowkface100/277", 277)         
    # glob_files("D:\lowkface100/278", 278)         
    # glob_files("D:\lowkface100/279", 279)         
    # glob_files("D:\lowkface100/280", 280)         
    # glob_files("D:\lowkface100/281", 281)         
    # glob_files("D:\lowkface100/282", 282)         
    # glob_files("D:\lowkface100/283", 283)         
    # glob_files("D:\lowkface100/284", 284)         
    # glob_files("D:\lowkface100/285", 285)         
    # glob_files("D:\lowkface100/286", 286)         
    # glob_files("D:\lowkface100/287", 287)         
    # glob_files("D:\lowkface100/288", 288)         
    # glob_files("D:\lowkface100/289", 289)         
    # glob_files("D:\lowkface100/290", 290)         
    # glob_files("D:\lowkface100/291", 291)         
    # glob_files("D:\lowkface100/292", 292)         
    # glob_files("D:\lowkface100/293", 293)         
    # glob_files("D:\lowkface100/294", 294)         
    # glob_files("D:\lowkface100/295", 295)         
    # glob_files("D:\lowkface100/296", 296)         
    # glob_files("D:\lowkface100/297", 297)         
    # glob_files("D:\lowkface100/298", 298)         
    # glob_files("D:\lowkface100/299", 299)         
    # glob_files("D:\lowkface100/300", 300)         
    # glob_files("D:\lowkface100/301", 301)         
    # glob_files("D:\lowkface100/302", 302)         
    # glob_files("D:\lowkface100/303", 303)         
    # glob_files("D:\lowkface100/304", 304)         
    # glob_files("D:\lowkface100/305", 305)         
    # glob_files("D:\lowkface100/306", 306)         
    # glob_files("D:\lowkface100/307", 307)         
    # glob_files("D:\lowkface100/308", 308)         
    # glob_files("D:\lowkface100/309", 309)         
    # glob_files("D:\lowkface100/310", 310)         
    # glob_files("D:\lowkface100/311", 311)         
    # glob_files("D:\lowkface100/312", 312)         
    # glob_files("D:\lowkface100/313", 313)         
    # glob_files("D:\lowkface100/314", 314)         
    # glob_files("D:\lowkface100/315", 315)         
    # glob_files("D:\lowkface100/316", 316)         
    # glob_files("D:\lowkface100/317", 317)         
    # glob_files("D:\lowkface100/318", 318)         
    # glob_files("D:\lowkface100/319", 319)         
    # glob_files("D:\lowkface100/320", 320)         
    # glob_files("D:\lowkface100/321", 321)         
    # glob_files("D:\lowkface100/322", 322)         
    # glob_files("D:\lowkface100/323", 323)         
    # glob_files("D:\lowkface100/324", 324)         
    # glob_files("D:\lowkface100/325", 325)         
    # glob_files("D:\lowkface100/326", 326)         
    # glob_files("D:\lowkface100/327", 327)         
    # glob_files("D:\lowkface100/328", 328)         
    # glob_files("D:\lowkface100/329", 329)         
    # glob_files("D:\lowkface100/330", 330)         
    # glob_files("D:\lowkface100/331", 331)         
    # glob_files("D:\lowkface100/332", 332)         
    # glob_files("D:\lowkface100/333", 333)         
    # glob_files("D:\lowkface100/334", 334)         
    # glob_files("D:\lowkface100/335", 335)         
    # glob_files("D:\lowkface100/336", 336)         
    # glob_files("D:\lowkface100/337", 337)         
    # glob_files("D:\lowkface100/338", 338)         
    # glob_files("D:\lowkface100/339", 339)         
    # glob_files("D:\lowkface100/340", 340)         
    # glob_files("D:\lowkface100/341", 341)         
    # glob_files("D:\lowkface100/342", 342)         
    # glob_files("D:\lowkface100/343", 343)         
    # glob_files("D:\lowkface100/344", 344)         
    # glob_files("D:\lowkface100/345", 345)         
    # glob_files("D:\lowkface100/346", 346)         
    # glob_files("D:\lowkface100/347", 347)         
    # glob_files("D:\lowkface100/348", 348)         
    # glob_files("D:\lowkface100/349", 349)         
    # glob_files("D:\lowkface100/350", 350)         
    # glob_files("D:\lowkface100/351", 351)         
    # glob_files("D:\lowkface100/352", 352)         
    # glob_files("D:\lowkface100/353", 353)         
    # glob_files("D:\lowkface100/354", 354)         
    # glob_files("D:\lowkface100/355", 355)         
    # glob_files("D:\lowkface100/356", 356)         
    # glob_files("D:\lowkface100/357", 357)         
    # glob_files("D:\lowkface100/358", 358)         
    # glob_files("D:\lowkface100/359", 359)         
    # glob_files("D:\lowkface100/360", 360)         
    # glob_files("D:\lowkface100/361", 361)         
    # glob_files("D:\lowkface100/362", 362)         
    # glob_files("D:\lowkface100/363", 363)         
    # glob_files("D:\lowkface100/364", 364)         
    # glob_files("D:\lowkface100/365", 365)         
    # glob_files("D:\lowkface100/366", 366)         
    # glob_files("D:\lowkface100/367", 367)         
    # glob_files("D:\lowkface100/368", 368)         
    # glob_files("D:\lowkface100/369", 369)         
    # glob_files("D:\lowkface100/370", 370)         
    # glob_files("D:\lowkface100/371", 371)         
    # glob_files("D:\lowkface100/372", 372)         
    # glob_files("D:\lowkface100/373", 373)         
    # glob_files("D:\lowkface100/374", 374)         
    # glob_files("D:\lowkface100/375", 375)         
    # glob_files("D:\lowkface100/376", 376)         
    # glob_files("D:\lowkface100/377", 377)         
    # glob_files("D:\lowkface100/378", 378)         
    # glob_files("D:\lowkface100/379", 379)         
    # glob_files("D:\lowkface100/380", 380)         
    # glob_files("D:\lowkface100/381", 381)         
    # glob_files("D:\lowkface100/382", 382)         
    # glob_files("D:\lowkface100/383", 383)         
    # glob_files("D:\lowkface100/384", 384)         
    # glob_files("D:\lowkface100/385", 385)         
    # glob_files("D:\lowkface100/386", 386)         
    # glob_files("D:\lowkface100/387", 387)         
    # glob_files("D:\lowkface100/388", 388)         
    # glob_files("D:\lowkface100/389", 389)         
    # glob_files("D:\lowkface100/390", 390)         
    # glob_files("D:\lowkface100/391", 391)         
    # glob_files("D:\lowkface100/392", 392)         
    # glob_files("D:\lowkface100/393", 393)         
    # glob_files("D:\lowkface100/394", 394)         
    # glob_files("D:\lowkface100/395", 395)         
    # glob_files("D:\lowkface100/396", 396)         
    # glob_files("D:\lowkface100/397", 397)         
    # glob_files("D:\lowkface100/398", 398)         
    # glob_files("D:\lowkface100/399", 399)         
        
                                                         # 파일로 저장하기
    print(outfile, len(x), "장 저장했습니다.")            # 600 장 저장했습니다.
    np.savez(outfile, x=x, y=y)  

def glob_files(path, label):            # path 내부의 이미지 읽어 들이기    
    files = glob.glob(path+ "/*.jpg")   # 폴더안의 파일들의 목록을 불러옴ex)glob('*.txt')
    # for문으로 모든 파일 색공간과 크기 변경
    num = 0
    for f in files:                                 # 200개의 이미지 3번
        # if num >= max_photo:break                   # 200개가 넘으면 멈춤
        num += 1
        # 이미지 파일 읽어 들이기 Image모듈 open함수 사용
        img = Image.open(f)
        img = img.convert("RGB")                     # 색공간 변환하기
        img = img.resize((photo_size, photo_size))   # (32, 32)로 크기 변경하기
        img = np.asarray(img)                        # modifying img itself
                                                     # array : modifying img a copy
        x.append(img)
        y.append(label)
# 엔트리 포인트 또는 메인이므로 main() 함수 실행    
if __name__ == '__main__':  
    main()

    

print(len(x))
# print(x)