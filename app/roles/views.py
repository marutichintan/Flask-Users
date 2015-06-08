#resource, resources, Resources
from flask import Blueprint, render_template, request,flash, redirect, url_for
from app.roles.models import Roles, RolesSchema

roles = Blueprint('roles', __name__)
#http://marshmallow.readthedocs.org/en/latest/quickstart.html#declaring-schemas
schema = RolesSchema()

#Roles
@roles.route('/' )
def role_index():
    roles = Roles.query.all()
    results = schema.dump(roles, many=True).data
    return render_template('/roles/index.html', results=results)

@roles.route('/add' , methods=['POST', 'GET'])
def role_add():
    if request.method == 'POST':
        #Validate form values by de-serializing the request, http://marshmallow.readthedocs.org/en/latest/quickstart.html#validation
        form_errors = schema.validate(request.form.to_dict())
        if not form_errors:
            name=request.form['name']
            role=Roles(name)
            return add(role, success_url = 'roles.role_index', fail_url = 'roles.role_add')
        else:
           flash(form_errors)

    return render_template('/roles/add.html')

@roles.route('/update/<int:id>' , methods=['POST', 'GET'])

def role_update (id):
    #Get role by primary key:
    role=Roles.query.get_or_404(id)
    if request.method == 'POST':
        form_errors = schema.validate(request.form.to_dict())
        if not form_errors:
           role.name = request.form['name']
           return update(role , id, success_url = 'roles.role_index', fail_url = 'roles.role_update')
        else:
           flash(form_errors)

    return render_template('/roles/update.html', role=role)


@roles.route('/delete/<int:id>' , methods=['POST', 'GET'])
def role_delete (id):
     role = Roles.query.get_or_404(id)
     return delete(role, fail_url = 'roles.role_index')


#CRUD FUNCTIONS
#Arguments  are data to add, function to redirect to if the add was successful and if not
def add (data, success_url = '', fail_url = ''):
    add = data.add(data)
    #if does not return any error
    if not add :
       flash("Add was successful")
       return redirect(url_for(success_url))
    else:
       message=add
       flash(message)
       return redirect(url_for(fail_url))


def update (data, id, success_url = '', fail_url = ''):

            update=data.update()
            #if does not return any error
            if not update :
              flash("Update was successful")
              return redirect(url_for(success_url))
            else:
               message=update
               flash(message)
               return redirect(url_for(fail_url, id=id))



def delete (data, fail_url=''):
     delete=data.delete(data)
     if not delete :
              flash("Delete was successful")

     else:
          message=delete
          flash(message)
     return redirect(url_for(fail_url))
