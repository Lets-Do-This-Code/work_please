from flask import render_template, flash, redirect, request
from app import app, db
from app.forms import NewOrderForm, EditOrderForm, RegisterForm
from app.models import customer, order, driver, register

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        Register = register(username=form.username.data, email=form.email.data, password=form.password.data, password2=form.password2.data)
        db.session.add(Register)
        db.session.commit()
        flash('Thank you for register with us')
        return redirect('/index')
    else:
        flash('Please try again')
    return render_template('register.html', title='Register', form=form)

@app.route('/orders')
def orders():
    Orders = order.query.all()
    return render_template('orders.html', title='Orders', rows=Orders)

@app.route('/neworder', methods=['GET', 'POST'])
def neworder():
    form = NewOrderForm()
    form.driver.choices = [(driver.driverID, driver.name) for driver in driver.query.all()]
    if form.validate_on_submit():
        Customer = customer(name=form.custname.data, phone=form.phone.data, address=form.address.data, suburb=form.suburb.data)
        Order = order(orderID=form.ordernum.data, driverID=form.driver.data)
        Customer.orders.append(Order)
        db.session.add(Customer)      
        db.session.add(Order)
        db.session.commit()
        flash('Congratulations, you have created a new order!')
        return redirect('/orders')
    return render_template('neworder.html', title='New Order', form=form)


@app.route('/editorder/<orderID>', methods=['GET', 'POST'])
def editorder(orderID):
    selectedOrder = order.query.filter_by(orderID=orderID).first()
    form = EditOrderForm(driver=selectedOrder)
    form.driver.choices = [(driver.driverID, driver.name) for driver in driver.query.all()]
    if form.validate_on_submit():
        selectedOrder.driverID = form.driver.data
        selectedOrder.orderingCust.name = form.name.data
        selectedOrder.orderingCust.phone = form.phone.data
        selectedOrder.orderingCust.address = form.address.data
        selectedOrder.orderingCust.suburb = form.suburb.data
        db.session.commit()
        flash('Congratulations, you have edited an order!')
        return redirect('/orders')
    elif request.method == 'GET':
        form.driver.data = selectedOrder.placedWithDriver.driverID
        form.orderID.data = selectedOrder.orderID
        form.name.data = selectedOrder.orderingCust.name
        form.phone.data = selectedOrder.orderingCust.phone
        form.address.data = selectedOrder.orderingCust.address
        form.suburb.data = selectedOrder.orderingCust.suburb
    return render_template('editorder.html', title='Edit Order', form=form)