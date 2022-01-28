import validator from "validator";

export function loginDto({ correo, password }) {
  //isStrongPassword > longitud min 8 caracters, almenso al 1 n
  //el validador hace la validacion siempre y cuando sea un string, si no un sitrng emitira un error pero la validacion retornara un boolean
  if (!validator.isEmail(correo)) {
    throw Error("El correo deve ser un correo valido");
  }
  if (!validator.isStrongPassword(password)) {
    throw Error(
      "La contraseña no es lo suficientemente segura, debe tener al menos una mayuscula ,una minuscula, un numero, un simbolo y una longitud min de 8 caracteres"
    );
  }
  return correo, password;
}
