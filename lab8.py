import csv

def stage1():
   with open('D:/movies.csv - movies.csv.csv',encoding='utf-8') as file:
    reader = csv.reader(file) 
    col=-1
    stu=-1
    list1=[]
    for row in reader:
        list1.append(row)
    for j in list1:
        col=col+1
        for i in j:
           stu=stu+1
           if stu==5:
              del(list1[col][stu])
        stu=-1
    col=-1
    res=[]
    for row in list1:
      del(row[-1])
      row[4]=[row[4]]
      res.append(row)
    print(res)
    
def stage2():
   with open('D:/movies.csv - movies.csv.csv',encoding='utf-8') as file:
    reader = csv.reader(file)
    films=[]
    for r in reader:
        films.append(r)
    num=0
    for row in range(len(films)):
        if row==0:
          print('{:<35}  | {}  |  | {} |   | {} |  | {} | | {} |'.format(films[row][0],films[row][1],films[row][2],films[row][3],films[row][5],films[row][6]))
          print('-'*114)
        else:
          films[row][2]=float(films[row][2])
          print('{:<35}  | {} |  |   {:.2f}  |   | {:>7}     |  |{:>13}   | |{:>13.2f}  |'.format(films[row][0],films[row][1],films[row][2],films[row][3],films[row][5],float(films[row][6])))

def stage3():
   with open('D:/movies.csv - movies.csv.csv',encoding='utf-8') as file:
    reader = csv.reader(file)
    res=[]
    ans1=[]
    ans2=[]
    ans3=[]
    answer=[]
    for row in reader:
        res.append(row)
    for i in range(len(res)):
        if i==0:
            pass
        else:
            ans1.append(float(res[i][2]))
            ans2.append(float(res[i][5]))
            ans3.append(float(res[i][6]))
    ans1.sort(reverse = True)
    ans2.sort(reverse = True)
    ans3.sort(reverse = True)
    
    ans1.insert(0,res[0][2])
    ans2.insert(0,res[0][5])
    ans3.insert(0,res[0][6])
    
    answer.append(ans1)
    answer.append(ans2)
    answer.append(ans3)

    sor1=[]
    sor2=[]
    sor3=[]
    for a in range(len(ans1)):
        for j in range(len(res)):
            if a==0 & j==0:
                pass
            else:
                if j!=0:
                   if ans1[a] == float(res[j][2]):
                       del(res[j][4])
                       sor1.append(res[j])
                   if ans2[a] == float(res[j][5]):
                       sor2.append(res[j])
                   if ans3[a] == float(res[j][-1]):
                       sor3.append(res[j])
    del(res[0][4])
    sor1.insert(0,res[0])
    sor2.insert(0,res[0])
    sor3.insert(0,res[0])
    
    for j in range(len(sor1)):
        if j==0:
           print('{:<35} | {}  | {} | {} | {} | {} |'.format(sor1[j][0],sor1[j][1],sor1[j][2],sor1[j][3],sor1[j][4],sor1[j][5]))
           print('-'*101)
        else:
            print('{:<35} | {} |   {:.2f}  | {:>7}     |{:>13}   | {:>13.2f} |'.format(sor1[j][0],sor1[j][1],float(sor1[j][2]),sor1[j][3],sor1[j][4],float(sor1[j][5])))

    print('*'*101)

    for j in range(len(sor2)):
        if j==0:
           print('{:<35} | {}  | {} | {} | {} | {} |'.format(sor2[j][0],sor2[j][1],sor2[j][2],sor2[j][3],sor2[j][4],sor2[j][5]))
           print('-'*101)
        else:
            print('{:<35} | {} |   {:.2f}  | {:>7}     |{:>13}   | {:>13.2f} |'.format(sor2[j][0],sor2[j][1],float(sor2[j][2]),sor2[j][3],sor2[j][4],float(sor2[j][5])))
    
    print('*'*101)

    for j in range(len(sor3)):
        if j==0:
           print('{:<35} | {}  | {} | {} | {} | {} |'.format(sor3[j][0],sor3[j][1],sor3[j][2],sor3[j][3],sor3[j][4],sor3[j][5]))
           print('-'*101)
        else:
            print('{:<35} | {} |   {:.2f}  | {:>7}     |{:>13}   | {:>13.2f} |'.format(sor3[j][0],sor3[j][1],float(sor3[j][2]),sor3[j][3],sor3[j][4],float(sor3[j][5])))

def sr(num):
    return float(sum(num)/len(num))
  
def stage4():
   with open('D:/movies.csv - movies.csv.csv',encoding='utf-8') as file:
    reader = csv.reader(file)
    res=[]
    answer=[]
    num=0
    budget=[]
    l=[]
    collect=[]
    ret=[]
    cost=[]
    genres=[]
    itog=[]
    inend=[]
    end=[]
    for row in reader:
        res.append(row)
        itog.append(row)
    
    for i in range(len(itog)):
        inend=str(itog[i][2])+';'+str(itog[i][3])+';'+str(itog[i][4])
        inend=inend.split(';')
        end.append(inend)
    
    for i in range(len(res)):
        genres.append(res[i][4])
        del(res[i][4])
        if i!=0:
            num= float(res[i][-1]) - float(res[i][4])
            answer.append(num)
            l.append(int(res[i][3]))
            budget.append(float(res[i][4]))
            collect.append(float(res[i][-1]))
            ret.append(float(res[i][2]))
            
        else:
            pass
    
    answer.sort(reverse = True)
    sor_ans=[]
    val=0
    del(genres[0])
    gen=[]
    for g in range(len(genres)):
        if ',' in genres[g]:
           
           genres[g]=genres[g].split(', ')
           for row in genres[g]:
               gen.append(row)
        else:
           gen.append(genres[g])
    ja=[]
    janr=[]
    
    for col in set(gen):
        ja =str(col) + ',' + str(gen.count(col))
        ja=ja.split(',')
        janr.append(ja)
       
    janr.sort(key=lambda n: int(n[1]), reverse=True)
    
    for j in range(len(answer)):
        for i in range(len(res)):
            if i!=0:
                num= float(res[i][-1]) - float(res[i][4])
                if answer[j]==num:
                    res[i].append(answer[j]) 
                    sor_ans.append(res[i])
            else:
               pass

   res[0].append('Прибыль')
   sor_ans.insert(0,res[0])
  
   value=0
   ROI=[]
   for i in range(len(sor_ans)):
       if i!=0:
          value=float(sor_ans[i][-1])/float(sor_ans[i][4])
          cost.append(float(sor_ans[i][4])/float(sor_ans[i][3])) #бюджет за минуту
          ROI.append(value)
   
   for j in range(len(sor_ans)):
       if j==0:
          print('{:<35} | {}  | {} | {} | {} | {} |  {}  |'.format(sor_ans[j][0],sor_ans[j][1],sor_ans[j][2],sor_ans[j][3],sor_ans[j][4],sor_ans[j][5],sor_ans[j][6]))
          print('-'*113)
       else:
          pass
          print('{:<35} | {} |   {:.2f}  | {:>7}     |{:>13}   |{:>13.2f}  |  {:.2f}   |'.format(sor_ans[j][0],sor_ans[j][1],float(sor_ans[j][2]),sor_ans[j][3],sor_ans[j][4],float(sor_ans[j][5]),float(sor_ans[j][6])))
   
   sp_genres=[]
   for i in range(len(sor_ans)):
       for j in range(len(end)):
           if i!=0 and j!=0:
              if sor_ans[i][2] == end[j][0] and sor_ans[i][3] == end[j][1]:
                  sp_genres.append(end[j][2])
   sp_genres.insert(0,'Жанр')       
   
   i_sp=[]
   itog_sp=[]
   for i in range(len(sp_genres)):
       if i!=0:
          i_sp=str(sp_genres[i])+';'+str(sor_ans[i][2])+';'+str(sor_ans[i][3])+';'+str(ROI[i-1])+';'+str(cost[i-1])
          i_sp=i_sp.split(';')
          itog_sp.append(i_sp)
       else:
           i_sp='Жанр'+';'+'Рейтинг'+';'+'Длина'+';'+'ROI'+';'+'Бюджет за минуту'
           i_sp=i_sp.split(';')
           itog_sp.append(i_sp)
  
   print('*'*120)        
   print('Средний бюджет фильмов: ', sr(budget))
   print('Средняя величина сборов: ', sr(collect))
   print('Средняя длина фильмов: ', sr(l))
   print('Средняя прибыль фильмов: ', sr(answer))
   print('Средный рейтинг фильмов: ', sr(ret))
   print('*'*120)

   column=0
   for i in range(len(janr)):
       if column==0:
           print(' {:<11} | {} |'.format('Жанр','Количество'))
           print('-'*27)
           column=column+1
       print(' {:<11} |      {}     |'.format(janr[i][0],janr[i][1]))

   
   for i in range(len(itog_sp)):
       if i==0:
           print('*'*120)
           print('{}                                      | {} | {} |   {}   | {} |'.format(itog_sp[i][0],itog_sp[i][1],itog_sp[i][2],itog_sp[i][3],itog_sp[i][4]))
           print('-'*100)
       else:
           print('{:<41} |   {:.2f}  |   {} | {:>7.3f} |     {:>7.3f}      |'.format(itog_sp[i][0],float(itog_sp[i][1]),itog_sp[i][2],float(itog_sp[i][3]),float(itog_sp[i][4])))
   print('*'*120)

   
stage3()
