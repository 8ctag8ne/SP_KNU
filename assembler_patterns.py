from Tokens import TokenType

ASSEMBLER_PATTERNS = [
    # Коментарі
    (r';.*', TokenType.COMMENT),

    # Рядкові константи
    (r'\"[^\"]*\"', TokenType.STRING),
    (r'\'[^\']*\'', TokenType.STRING),

    # Директиви
    (
    r'\.(MODEL|STACK|DATA|CODE|SEGMENT|ENDS|PROC|ENDP|DB|DW|DD|DQ|DT|DF|DP|END|ASSUME|ORG|OFFSET|PTR|TYPE|SIZE|LENGTH|EQU|=|\$)',
    TokenType.DIRECTIVE),

    # Регістри
    (r'\b(AX|BX|CX|DX|AL|BL|CL|DL|AH|BH|CH|DH|SI|DI|SP|BP|CS|DS|ES|SS|FS|GS|'
     r'EAX|EBX|ECX|EDX|ESI|EDI|ESP|EBP|CR0|CR2|CR3|DR0|DR1|DR2|DR3|DR6|DR7|'
     r'TR6|TR7|ST\([0-7]\)|ST)\b',
     TokenType.REGISTER),

    # x86 інструкції
    (r'\b(AAA|AAD|AAM|AAS|ADC|ADD|AND|CALL|CBW|CLC|CLD|CLI|CMC|CMP|CMPSB|'
     r'CMPSW|CWD|DAA|DAS|DEC|DIV|ESC|HLT|IDIV|IMUL|IN|INC|INT|INTO|IRET|JA|'
     r'JAE|JB|JBE|JC|JCXZ|JE|JG|JGE|JL|JLE|JMP|JNA|JNAE|JNB|JNBE|JNC|JNE|'
     r'JNG|JNGE|JNL|JNLE|JNO|JNP|JNS|JNZ|JO|JP|JPE|JPO|JS|JZ|LAHF|LDS|LEA|'
     r'LES|LODSB|LODSW|LOOP|LOOPE|LOOPNE|LOOPNZ|LOOPZ|MOV|MOVSB|MOVSW|MUL|'
     r'NEG|NOP|NOT|OR|OUT|POP|POPF|PUSH|PUSHF|RCL|RCR|RET|RETF|RETN|ROL|ROR|'
     r'SAHF|SAL|SAR|SBB|SCASB|SCASW|SHL|SHR|STC|STD|STI|STOSB|STOSW|SUB|TEST|'
     r'WAIT|XCHG|XLAT|XOR)\b',
     TokenType.INSTRUCTION),

    # FPU інструкції
    (r'\b(F2XM1|FABS|FADD|FADDP|FBLD|FBSTP|FCHS|FCLEX|FCOM|FCOMP|FCOMPP|'
     r'FDECSTP|FDISI|FDIV|FDIVP|FDIVR|FDIVRP|FENI|FFREE|FIADD|FICOM|FICOMP|'
     r'FIDIV|FIDIVR|FILD|FIMUL|FINCSTP|FINIT|FIST|FISTP|FISUB|FISUBR|FLD|'
     r'FLD1|FLDCW|FLDENV|FLDL2E|FLDL2T|FLDLG2|FLDLN2|FLDPI|FLDZ|FMUL|FMULP|'
     r'FNCLEX|FNDISI|FNENI|FNINIT|FNOP|FNSAVE|FNSTCW|FNSTENV|FNSTSW|FPATAN|'
     r'FPREM|FPTAN|FRNDINT|FRSTOR|FSAVE|FSCALE|FSQRT|FST|FSTCW|FSTENV|FSTP|'
     r'FSTSW|FSUB|FSUBP|FSUBR|FSUBRP|FTST|FWAIT|FXAM|FXCH|FXTRACT|FYL2X|'
     r'FYL2XP1)\b',
     TokenType.INSTRUCTION),

    # MMX/SSE інструкції
    (r'\b(ADDPD|ADDPS|ADDSD|ADDSS|ANDNPD|ANDNPS|ANDPD|ANDPS|CMPPD|CMPPS|'
     r'CMPSD|CMPSS|COMISD|COMISS|CVTDQ2PD|CVTDQ2PS|CVTPD2DQ|CVTPD2PI|'
     r'CVTPD2PS|CVTPI2PD|CVTPI2PS|CVTPS2DQ|CVTPS2PD|CVTPS2PI|CVTSD2SI|'
     r'CVTSD2SS|CVTSI2SD|CVTSI2SS|CVTSS2SD|CVTSS2SI|CVTTPD2DQ|CVTTPD2PI|'
     r'CVTTPS2DQ|CVTTPS2PI|CVTTSD2SI|CVTTSS2SI|DIVPD|DIVPS|DIVSD|DIVSS|'
     r'MAXPD|MAXPS|MAXSD|MAXSS|MINPD|MINPS|MINSD|MINSS|MOVAPD|MOVAPS|MOVD|'
     r'MOVHPD|MOVHPS|MOVLHPS|MOVLPD|MOVLPS|MOVMSKPD|MOVMSKPS|MOVQ|MOVSD|'
     r'MOVSS|MOVUPD|MOVUPS|MULPD|MULPS|MULSD|MULSS|ORPD|ORPS|PACKSSDW|'
     r'PACKSSWB|PACKUSWB|PADDB|PADDD|PADDQ|PADDSB|PADDSW|PADDUSB|PADDUSW|'
     r'PADDW|PAND|PANDN|PAVGB|PAVGW|PCMPEQB|PCMPEQD|PCMPEQW|PCMPGTB|'
     r'PCMPGTD|PCMPGTW|PEXTRW|PINSRW|PMADDWD|PMAXSW|PMAXUB|PMINSW|PMINUB|'
     r'PMOVMSKB|PMULHUW|PMULHW|PMULLW|PMULUDQ|POR|PSADBW|PSHUFD|PSHUFHW|'
     r'PSHUFLW|PSHUFW|PSLLD|PSLLDQ|PSLLQ|PSLLW|PSRAD|PSRAW|PSRLD|PSRLDQ|'
     r'PSRLQ|PSRLW|PSUBB|PSUBD|PSUBQ|PSUBSB|PSUBSW|PSUBUSB|PSUBUSW|PSUBW|'
     r'PUNPCKHBW|PUNPCKHDQ|PUNPCKHQDQ|PUNPCKHWD|PUNPCKLBW|PUNPCKLDQ|'
     r'PUNPCKLQDQ|PUNPCKLWD|PXOR|RCPPS|RCPSS|RSQRTPS|RSQRTSS|SHUFPD|SHUFPS|'
     r'SQRTPD|SQRTPS|SQRTSD|SQRTSS|SUBPD|SUBPS|SUBSD|SUBSS|UCOMISD|UCOMISS|'
     r'UNPCKHPD|UNPCKHPS|UNPCKLPD|UNPCKLPS|XORPD|XORPS)\b',
     TokenType.INSTRUCTION),

    # Мітки
    (r'^[A-Za-z_][A-Za-z0-9_]*:', TokenType.LABEL),

    # Числа з плаваючою комою
    (r'-?\d+\.\d+[Ee][+-]?\d+', TokenType.NUMBER),  # науковий запис (1.23E-4)
    (r'-?\d+\.\d+', TokenType.NUMBER),  # десяткові дроби (1.23)

    # Цілі числа
    (r'\b[0-9][0-9A-Fa-f]*[Hh]\b', TokenType.NUMBER),  # шістнадцяткові з H/h в кінці
    (r'\b[0-9]+[0-9A-Fa-f]*F\b', TokenType.NUMBER),  # шістнадцяткові з F в кінці
    (r'\b0x[0-9A-Fa-f]+\b', TokenType.NUMBER),  # шістнадцяткові (0x...)
    (r'\b[0-9]+d?\b', TokenType.NUMBER),  # десяткові
    (r'\b[01]+b\b', TokenType.NUMBER),  # двійкові
    (r'\b[0-7]+[oOqQ]\b', TokenType.NUMBER),  # вісімкові

    # Оператори
    (r'[\+\-\*\/\[\]\(\),\:,\=]', TokenType.OPERATOR),

    # Спеціальні символи
    (r'[\$\?\@\#\&\|\^\%\!]', TokenType.OPERATOR),

    # Ідентифікатори
    (r'[A-Za-z_][A-Za-z0-9_]*', TokenType.IDENTIFIER),
]