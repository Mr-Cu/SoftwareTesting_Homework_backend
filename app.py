# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 18:28
# @Author  : STY
# @Email   : 1455670697@qq.com
# @File    : app.py
# @Software: PyCharm
import json
import os
from flask import Flask, make_response, request, redirect, url_for, send_from_directory
import pandas as pd

import atmsystem.atmsystem
import charges.charges as charges
import computer.computer as computer
import sales.sales
import triangle.triangle as triangle
import thecalendar.thecalendar as thecalendar
from flask_cors import CORS
from myutils import *

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/question1', methods=['POST', 'GET'])
def question1():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[5] = 0
    df[6] = 0
    for i in range(df.shape[0]):
        df.loc[i, 5] = triangle.compute(df[1][i], df[2][i], df[3][i])
        if str(df[4][i]) != str(df[5][i]):
            df.loc[i, 6] = "未通过测试"
        else:
            df.loc[i, 6] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


@app.route('/question2', methods=['POST', 'GET'])
def question2():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[4] = 0
    df[5] = 0
    for i in range(df.shape[0]):
        df.loc[i, 4] = charges.compute(df[1][i], df[2][i])
        if str(df[3][i]) != str(df[4][i]):
            df.loc[i, 5] = "未通过测试"
        else:
            df.loc[i, 5] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


@app.route('/question3', methods=['POST', 'GET'])
def question3():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[5] = 0
    df[6] = 0
    for i in range(df.shape[0]):
        df.loc[i, 5] = computer.compute(df[1][i], df[2][i], df[3][i])
        if str(df[4][i]) != str(df[5][i]):
            df.loc[i, 6] = "未通过测试"
        else:
            df.loc[i, 6] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


@app.route('/question4', methods=['POST', 'GET'])
def question4():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[5] = 0
    df[6] = 0
    for i in range(df.shape[0]):
        df.loc[i, 5] = thecalendar.calendar_atom([df[1][i], df[2][i], df[3][i]])
        if str(df[4][i]) != str(df[5][i]):
            df.loc[i, 6] = "未通过测试"
        else:
            df.loc[i, 6] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


@app.route('/question5', methods=['POST', 'GET'])
def question5():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[3] = 0
    df[4] = 0
    for i in range(df.shape[0]):
        df.loc[i, 3] = atmsystem.atmsystem.printer_atom([df[1][i]])
        if str(df[2][i]) != str(df[3][i]):
            df.loc[i, 4] = "未通过测试"
        else:
            df.loc[i, 4] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


@app.route('/question6', methods=['POST', 'GET'])
def question6():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[6] = 0
    df[7] = 0
    df[8] = 0
    for i in range(df.shape[0]):
        df.loc[i, 6] = sales.sales.sales_atom([df[1][i], df[2][i], df[3][i]])
        df.loc[i, 7] = sales.sales.sales_atom_1([df[1][i], df[2][i], df[3][i]])
        if str(df[4][i]) != str(df[6][i]):
            df.loc[i, 8] = "未通过测试"
        else:
            if df[5][i] != "没有输出值" and df[5][i] != "输入超出范围":
                tmp = float(df[5][i])
            else:
                tmp = df[5][i]
            if str(tmp) != str(df[7][i]):
                df.loc[i, 8] = "未通过测试"
            else:
                df.loc[i, 8] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
