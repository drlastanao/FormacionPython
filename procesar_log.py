import re
from dataclasses import dataclass
from typing import Generator, Literal, Optional, TypedDict

# ==========================================================
# 1. TYPING & DATA MODELS (Estructura y Tipado Estático)
# ==========================================================

# Literal restringe los valores permitidos exactamente a estos strings
LogLevel = Literal["INFO", "WARN", "ERROR", "FATAL"]


@dataclass(frozen=True)
class LogEntry:
    """Clase inmutable (frozen=True) para representar un registro de log parseado.

    Garantiza inmutabilidad y seguridad al pasarla entre funciones.
    """

    timestamp: str
    level: LogLevel
    message: str
    details: str


class ErrorSummary(TypedDict):
    """TypedDict define la estructura estricta que debe tener un diccionario

    sirviendo como interfaz de datos.
    """

    total_errors: int
    error_codes: list[int]
    critical_logs: list[str]


# ==========================================================
# 2. GENERADORES (Procesamiento Eficiente en Memoria)
# ==========================================================


def read_log_file(filepath: str) -> Generator[str, None, None]:
    """Generador que lee un archivo línea por línea (Lazy Evaluation).

    A diferencia de readlines(), 'yield' retiene solo 1 línea en memoria RAM,
    permitiendo procesar archivos de gigabytes sin consumo excesivo.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line_clean = line.strip()
            if line_clean:  # Omitir líneas vacías
                yield line_clean


# ==========================================================
# 3. PATTERN MATCHING & COMPREHENSIONS (Analizador)
# ==========================================================

LOG_PATTERN = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+?)(?: - (.+))?$"
)


def parse_log_line(line: str) -> Optional[LogEntry]:
    """Convierte una línea de texto en un objeto LogEntry.

    Utiliza Pattern Matching (Python 3.10+) para desestructuración y validación
    de tipo.
    """
    match = LOG_PATTERN.match(line)
    if not match:
        return None

    timestamp, level_str, message, details = match.groups()

    # Structural Pattern Matching sobre el nivel extraído
    match level_str:
        case "INFO" | "WARN" | "ERROR" | "FATAL" as level:
            # 'as level' asigna el valor coincidente y el type checker
            # deduce que 'level' satisface la restricción LogLevel
            return LogEntry(
                timestamp=timestamp,
                level=level,
                message=message,
                details=details or "",
            )
        case _:
            # Caso wildcard (descarte de niveles no reconocidos)
            return None


def process_logs(filepath: str) -> ErrorSummary:
    """Procesa el flujo completo mediante pipeline de generadores y

    comprehensions.
    """
    # Pipeline de evaluacion perezosa (no lee nada hasta ser iterado)
    raw_lines = read_log_file(filepath)
    parsed_entries = (parse_log_line(line) for line in raw_lines)

    # List comprehension: Filtra solo las entradas válidas y críticas
    error_entries: list[LogEntry] = [
        entry
        for entry in parsed_entries
        if entry is not None and entry.level in ("ERROR", "FATAL")
    ]

    # Extracción de códigos numéricos de error
    error_codes: list[int] = []
    for entry in error_entries:
        if "err_code=" in entry.details:
            code_str = entry.details.split("err_code=")[1].split()[0]
            if code_str.isdigit():
                error_codes.append(int(code_str))

    # Formateo rápido de errores fatales
    critical_logs: list[str] = [
        f"[{e.timestamp}] {e.message}"
        for e in error_entries
        if e.level == "FATAL"
    ]

    return {
        "total_errors": len(error_entries),
        "error_codes": error_codes,
        "critical_logs": critical_logs,
    }


# ==========================================================
# 4. EJECUCIÓN
# ==========================================================

if __name__ == "__main__":
    log_file_path = "logs.txt"
    summary = process_logs(log_file_path)

    print("--- RESUMEN DE ERRORES ---")
    print(f"Total de Errores: {summary['total_errors']}")
    print(f"Códigos capturados: {summary['error_codes']}")
    print(f"Logs Críticos (FATAL): {summary['critical_logs']}")