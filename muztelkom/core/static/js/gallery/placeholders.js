let form_fields = document.getElementsByTagName('input');
form_fields[1].placeholder='Model telefonu';
form_fields[2].placeholder='Opis telefonu';

for (let field in form_fields){
    form_fields[field].className += ' form-control'
}