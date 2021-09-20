from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def graph():

    
    num = request.args.get('Info')
    if num == None:
        num= '1'
    
    
    
    filename = 'finalized_model.sav'

    loaded_model = pickle.load(open(filename, 'rb'))
    
    abn = int(num)
    pred_uc = loaded_model.get_forecast(steps=abn)


    pred_ci = pred_uc.conf_int()

    lower = list(pred_ci.iloc[:, 0])

    pred_ci.iloc[:, 1] = pred_ci.iloc[:, 1] - 5

    upper =list(pred_ci.iloc[:, 1])

    mean = (pred_ci.iloc[:, 0] + pred_ci.iloc[:, 1])
    avg = list(mean/2)
    lower = [int(a) for a in lower]
    upper = [int(a) for a in upper]
    avg = [int(a) for a in avg]

 
    if num == '1':
        year = ['MAY 2021']
        
  
    if num == '2':
        year = ['MAY 2021','JUNE 2021'] 
    if num == '3':
        year = ['MAY 2021','JUNE 2021','JULY 2021']  
    if num == '4':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021']  
    if num == '5':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021']   
    if num == '6':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021']   
    if num == '7':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021']      
    if num == '8':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021']
    if num == '9':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2022']
    if num == '10':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2022','FEBRUARY 2022']
    if num == '11':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2022','FEBRUARY 2022','MARCH 2022']   
    if num == '12':
        year = ['MAY 2021','JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2022','FEBRUARY 2022','MARCH 2022','APRIL 2022']      
    
    finallist = []
    for i in range(abn):
        vm = (year[i],lower[i],upper[i],avg[i])
        finallist.append(vm)
        
    
    
    


   
    return render_template('graph.html', labels=year, ca=lower, charge=upper, ecart=avg,values = finallist)
    #return jsonify(labels=labels, ca=ca, charge=charge, ecart=ecart, info=info)



        
        


if __name__ == '__main__':

    app.run(debug=True,port=8006)
