let form_fields = document.getElementsByTagName('input');
form_fields[1].placeholder='Temat artykułu';

for (let field in form_fields){
    form_fields[field].className += ' form-control'
}