import jwt from "jsonwebtoken";
export function verificarToken(token) {
  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET);
    return payload;
  } catch (error) {
    return error;
  }
}

export function validarUsuario(req, res, next) {
  // meddleware
  // es un intermediario entre el cliente y el controlador final
  if (!req.headers.authorization) {
    return res.status(401).json({
      message: "Se necesita una token para realizar la solicitud",
    });
  }
  const token = req.headers.authorization.split("")[1];
  if (resultado instanceof jwt.JsonWebTokenError) {
    return res.status(403).json({
      message: "la token es invalida , intente nuevamente",
    });
  }
  //   const resultado = verificarToken(token);
  next();
}
