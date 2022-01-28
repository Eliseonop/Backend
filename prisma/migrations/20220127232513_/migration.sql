/*
  Warnings:

  - You are about to alter the column `nombre` on the `productos` table. The data in that column could be lost. The data in that column will be cast from `Text` to `VarChar(100)`.
  - You are about to drop the `Usuario` table. If the table is not empty, all the data it contains will be lost.

*/
-- AlterTable
ALTER TABLE "productos" ALTER COLUMN "nombre" SET DATA TYPE VARCHAR(100);

-- DropTable
DROP TABLE "Usuario";

-- CreateTable
CREATE TABLE "usuarios" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT NOT NULL,
    "correo" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "tipo_usuario" "TipoUsuario" NOT NULL,

    CONSTRAINT "usuarios_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_id_key" ON "usuarios"("id");

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_correo_key" ON "usuarios"("correo");
