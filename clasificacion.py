import pandas as pd

def cie10_det(codigo):
    if pd.isna(codigo):
        return None
    codigo = str(codigo).strip().upper()

    if codigo.startswith('A00') or codigo.startswith('A01') or codigo.startswith('A02') or codigo.startswith('A03') or codigo.startswith('A04') or codigo.startswith('A05') or codigo.startswith('A06') or codigo.startswith('A07') or codigo.startswith('A08') or codigo.startswith('A09'):
        return 'Enfermedades infecciosas intestinales (A00-A09)'
    elif codigo.startswith(('A15', 'A16', 'A17', 'A18', 'A19')):
        return 'Tuberculosis (A15-A19)'
    elif codigo.startswith(('A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28')):
        return 'Ciertas zoonosis bacterianas (A20-A28)'
    elif codigo.startswith(('A30', 'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49')):
        return 'Otras enfermedades bacterianas (A30-A49)'
    elif codigo.startswith(('A50', 'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57', 'A58', 'A59', 'A60', 'A61', 'A62', 'A63', 'A64')):
        return 'Enfermedades de transmisión sexual (A50-A64)'
    elif codigo.startswith(('A65', 'A66', 'A67', 'A68', 'A69')):
        return 'Otras enfermedades debidas a espiroquetas (A65-A69)'
    elif codigo.startswith(('A70', 'A71', 'A72', 'A73', 'A74')):
        return 'Otras enfermedades causadas por clamidias (A70-A74)'
    elif codigo.startswith(('A75', 'A76', 'A77', 'A78', 'A79')):
        return 'Rickettsiosis (A75-A79)'
    elif codigo.startswith(('A80', 'A81', 'A82', 'A83', 'A84', 'A85', 'A86', 'A87', 'A88', 'A89')):
        return 'Infecciones virales del sistema nervioso central (A80-A89)'
    elif codigo.startswith(('A90', 'A91', 'A92', 'A93', 'A94', 'A95', 'A96', 'A97', 'A98', 'A99')):
        return 'Fiebres virales transmitidas por artrópodos y hemorrágicas (A90-A99)'
    elif codigo.startswith(('B00', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09')):
        return 'Infecciones virales con lesiones en piel y mucosas (B00-B09)'
    elif codigo.startswith(('B15', 'B16', 'B17', 'B18', 'B19')):
        return 'Hepatitis viral (B15-B19)'
    elif codigo.startswith(('B20', 'B21', 'B22', 'B23', 'B24')):
        return 'VIH (B20-B24)'
    elif codigo.startswith(('B25', 'B26', 'B27', 'B28', 'B29', 'B30', 'B31', 'B32', 'B33', 'B34')):
        return 'Otras enfermedades virales (B25-B34)'
    elif codigo.startswith(('B35', 'B36', 'B37', 'B38', 'B39', 'B40', 'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47', 'B48', 'B49')):
        return 'Micosis (B35-B49)'
    elif codigo.startswith(('B50', 'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57', 'B58', 'B59', 'B60', 'B61', 'B62', 'B63', 'B64')):
        return 'Protozoos (B50-B64)'
    elif codigo.startswith(('B65', 'B66', 'B67', 'B68', 'B69', 'B70', 'B71', 'B72', 'B73', 'B74', 'B75', 'B76', 'B77', 'B78', 'B79', 'B80', 'B81', 'B82', 'B83')):
        return 'Helmintiasis (B65-B83)'
    elif codigo.startswith(('B85', 'B86', 'B87', 'B88', 'B89')):
        return 'Pediculosis, acariasis y otras infestaciones (B85-B89)'
    elif codigo.startswith(('B90', 'B91', 'B92', 'B93', 'B94')):
        return 'Secuelas de enfermedades infecciosas (B90-B94)'
    elif codigo.startswith(('B95', 'B96', 'B97')):
        return 'Agentes bacterianos y virales (B95-B97)'
    elif codigo.startswith('B99'):
        return 'Otras enfermedades infecciosas (B99)'
    elif codigo.startswith(('C00', 'C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C30', 'C31', 'C32', 'C33', 'C34', 'C37', 'C38', 'C39', 'C40', 'C41', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C60', 'C61', 'C62', 'C63', 'C64', 'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73', 'C74', 'C75', 'C76', 'C77', 'C78', 'C79', 'C80', 'C81', 'C82', 'C83', 'C84', 'C85', 'C86', 'C87', 'C88', 'C89', 'C90', 'C91', 'C92', 'C93', 'C94', 'C95', 'C96', 'C97')):
        return 'Neoplasias malignas (C00-C97)'
    elif codigo.startswith(('D00', 'D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37', 'D38', 'D39', 'D40', 'D41', 'D42', 'D43', 'D44', 'D45', 'D46', 'D47', 'D48')):
        return 'Neoplasias in situ, benignas o inciertas (D00-D48)'
    elif codigo.startswith(('D50', 'D51', 'D52', 'D53')):
        return 'Anemias nutricionales (D50-D53)'
    elif codigo.startswith(('D55', 'D56', 'D57', 'D58', 'D59')):
        return 'Anemia hemolítica (D55-D59)'
    elif codigo.startswith(('D60', 'D61', 'D62', 'D63', 'D64')):
        return 'Aplasia y otras anemias (D60-D64)'
    elif codigo.startswith(('D65', 'D66', 'D67', 'D68')):
        return 'Defectos de la coagulación y otras afecciones hemorrágicas (D65-D68)'
    elif codigo.startswith('D69'):
        return 'Púrpura y otras afecciones hemorrágicas (D69)'
    elif codigo.startswith(('D70', 'D71', 'D72', 'D73', 'D74', 'D75', 'D76', 'D77')):
        return 'Otras enfermedades de la sangre y órganos hematopoyéticos (D70-D77)'
    elif codigo.startswith(('D80', 'D81', 'D82', 'D83', 'D84', 'D85', 'D86', 'D87', 'D88', 'D89')):
        return 'Ciertos desórdenes del sistema inmune (D80-D89)'
    elif codigo.startswith(('E00', 'E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27', 'E28', 'E29', 'E30', 'E31', 'E32', 'E34', 'E35')):
        return 'Enfermedades endocrinas (E00-E35)'
    elif codigo.startswith(('E40', 'E41', 'E42', 'E43', 'E44', 'E45', 'E46', 'E50', 'E51', 'E52', 'E53', 'E54', 'E55', 'E56', 'E58', 'E59', 'E60', 'E61', 'E62', 'E63', 'E64', 'E65', 'E66', 'E67', 'E68')):
        return 'Enfermedades nutricionales (E40-E68)'
    elif codigo.startswith(('E70', 'E71', 'E72', 'E73', 'E74', 'E75', 'E76', 'E77', 'E78', 'E79', 'E80', 'E83', 'E84', 'E85', 'E86', 'E87', 'E88', 'E89', 'E90')):
        return 'Trastornos metabólicos (E70-E90)'
    elif codigo.startswith(('F00', 'F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F09')):
        return 'Trastornos mentales orgánicos, incluidos los trastornos sintomáticos (F00-F09)'
    elif codigo.startswith(('F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19')):
        return 'Trastornos mentales y de comportamiento debidos al consumo de psicotrópicos (F10-F19)'
    elif codigo.startswith(('F20', 'F21', 'F22', 'F23', 'F24', 'F25', 'F28', 'F29')):
        return 'Esquizofrenia, trastornos esquizotípicos y trastornos delirantes (F20-F29)'
    elif codigo.startswith(('F30', 'F31', 'F32', 'F33', 'F34', 'F38', 'F39')):
        return 'Trastornos del estado de ánimo, trastornos afectivos (F30-F39)'
    elif codigo.startswith(('F40', 'F41', 'F42', 'F43', 'F44', 'F45', 'F48', 'F49')):
        return 'Trastornos neuróticos, relacionados con el estrés y somatomorfos (F40-F49)'
    elif codigo.startswith(('F50', 'F51', 'F52', 'F53', 'F54', 'F55', 'F59')):
        return 'Trastornos del comportamiento asociados a disfunciones fisiológicas y factores somáticos (F50-F59)'
    elif codigo.startswith(('F60', 'F61', 'F62', 'F63', 'F64', 'F65', 'F66', 'F68', 'F69')):
        return 'Trastornos de la personalidad y del comportamiento en adultos (F60-F69)'
    elif codigo.startswith(('F70', 'F71', 'F72', 'F73', 'F78', 'F79')):
        return 'Retraso mental (F70-F79)'
    elif codigo.startswith(('F80', 'F81', 'F82', 'F83', 'F84', 'F88', 'F89')):
        return 'Trastornos del desarrollo psicológico (F80-F89)'
    elif codigo.startswith(('F90', 'F91', 'F92', 'F93', 'F94', 'F95', 'F98')):
        return 'Trastornos emocionales y del comportamiento en la niñez o adolescencia (F90-F98)'
    elif codigo.startswith('F99'):
        return 'Trastornos mentales sin especificar (F99)'
    elif codigo.startswith(('G00', 'G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G07', 'G08', 'G09')):
        return 'Enfermedades inflamatorias del sistema nervioso central (G00-G09)'
    elif codigo.startswith(('G10', 'G11', 'G12', 'G13')):
        return 'Atrofias sistémicas con afección primaria del sistema nervioso central (G10-G13)'
    elif codigo.startswith(('G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26')):
        return 'Trastornos extrapiramidales y del movimiento (G20-G26)'
    elif codigo.startswith(('G30', 'G31', 'G32')):
        return 'Otras enfermedades degenerativas del sistema nervioso (G30-G32)'
    elif codigo.startswith(('G35', 'G36', 'G37')):
        return 'Enfermedades desmielinizantes del sistema nervioso central (G35-G37)'
    elif codigo.startswith(('G40', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47')):
        return 'Trastornos episódicos y paroxísticos (G40-G47)'
    elif codigo.startswith(('G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59')):
        return 'Trastornos de los nervios, de las raíces y de los plexos nerviosos (G50-G59)'
    elif codigo.startswith(('G60', 'G61', 'G62', 'G63', 'G64')):
        return 'Polineuropatías y otros trastornos del sistema nervioso periférico (G60-G64)'
    elif codigo.startswith(('G70', 'G71', 'G72', 'G73')):
        return 'Enfermedades musculares y de la unión neuromuscular (G70-G73)'
    elif codigo.startswith(('G80', 'G81', 'G82', 'G83')):
        return 'Parálisis cerebral y otros síndromes paralíticos (G80-G83)'
    elif codigo.startswith(('G90', 'G91', 'G92', 'G93', 'G94', 'G95', 'G96', 'G97', 'G98', 'G99')):
        return 'Otros trastornos del sistema nervioso (G90-G99)'
    elif codigo.startswith(('H00', 'H01', 'H02', 'H03', 'H04', 'H05', 'H06')):
        return 'Trastornos del párpado, aparato lagrimal y órbita (H00-H06)'
    elif codigo.startswith(('H10', 'H11', 'H12', 'H13')):
        return 'Trastornos de la conjuntiva (H10-H13)'
    elif codigo.startswith(('H15', 'H16', 'H17', 'H18', 'H19')):
        return 'Trastornos de la esclerótica y de la córnea (H15-H19)'
    elif codigo.startswith(('H20', 'H21', 'H22')):
        return 'Trastornos del iris y del cuerpo ciliar (H20-H22)'
    elif codigo.startswith(('H25', 'H26', 'H27', 'H28')):
        return 'Trastornos del cristalino (H25-H28)'
    elif codigo.startswith(('H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'H36')):
        return 'Trastornos de la coroides y la retina (H30-H36)'
    elif codigo.startswith(('H40', 'H41', 'H42')):
        return 'Glaucomas (H40-H42)'
    elif codigo.startswith(('H43', 'H44', 'H45')):
        return 'Trastornos del humor vítreo y del globo ocular (H43-H45)'
    elif codigo.startswith(('H46', 'H47', 'H48')):
        return 'Trastornos del nervio óptico y los campos visuales (H46-H48)'
    elif codigo.startswith(('H49', 'H50', 'H51', 'H52')):
        return 'Trastornos de músculos oculares, movimientos binoculares y refracción (H49-H52)'
    elif codigo.startswith(('H53', 'H54')):
        return 'Alteraciones visuales y ceguera (H53-H54)'
    elif codigo.startswith(('H55', 'H56', 'H57', 'H58', 'H59')):
        return 'Otros trastornos del ojo y anexos (H55-H59)'
    elif codigo.startswith(('H60', 'H61', 'H62')):
        return 'Enfermedades del oído externo (H60-H62)'
    elif codigo.startswith(('H65', 'H66', 'H67', 'H68', 'H69', 'H70', 'H71', 'H72', 'H73', 'H74', 'H75')):
        return 'Enfermedades del oído medio y del mastoides (H65-H75)'
    elif codigo.startswith(('H80', 'H81', 'H82', 'H83')):
        return 'Enfermedades del oído interno (H80-H83)'
    elif codigo.startswith(('H90', 'H91', 'H92', 'H93', 'H94', 'H95')):
        return 'Otros trastornos del oído (H90-H95)'
    elif codigo.startswith(('J00', 'J01', 'J02', 'J03', 'J04', 'J05', 'J06')):
        return 'Infecciones agudas de las vías respiratorias superiores (J00-J06)'
    elif codigo.startswith(('J09', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19')):
        return 'Gripe y Neumonía (J09-J19)'
    elif codigo.startswith(('J20', 'J21', 'J22')):
        return 'Enfermedades respiratorias inferiores agudas (J20-J22)'
    elif codigo.startswith(('J30', 'J31', 'J32', 'J33', 'J34', 'J35', 'J36', 'J37', 'J38', 'J39')):
        return 'Otras enfermedades de las vías respiratorias superiores (J30-J39)'
    elif codigo.startswith(('J40', 'J41', 'J42', 'J43', 'J44', 'J45', 'J46', 'J47')):
        return 'Enfermedades respiratorias inferiores crónicas (J40-J47)'
    elif codigo.startswith(('J60', 'J61', 'J62', 'J63', 'J64', 'J65', 'J66', 'J67', 'J68', 'J69', 'J70')):
        return 'Enfermedades del pulmón debidas a agentes externos (J60-J70)'
    elif codigo.startswith(('J80', 'J81', 'J82', 'J83', 'J84')):
        return 'Otras enfermedades respiratorias intersticiales (J80-J84)'
    elif codigo.startswith(('J85', 'J86')):
        return 'Condiciones supurativas y necróticas del tracto respiratorio inferior (J85-J86)'
    elif codigo.startswith(('J90', 'J91', 'J92', 'J93', 'J94')):
        return 'Otras enfermedades de la pleura (J90-J94)'
    elif codigo.startswith(('J95', 'J96', 'J97', 'J98', 'J99')):
        return 'Otras enfermedades del sistema respiratorio (J95-J99)'
    elif codigo.startswith(('K00', 'K01', 'K02', 'K03', 'K04', 'K05', 'K06', 'K07', 'K08', 'K09', 'K10', 'K11', 'K12', 'K13', 'K14')):
        return 'Enfermedades de la cavidad oral, glándulas salivales, mandíbula y maxilar (K00-K14)'
    elif codigo.startswith(('K20', 'K21', 'K22', 'K23', 'K24', 'K25', 'K26', 'K27', 'K28', 'K29', 'K30', 'K31')):
        return 'Enfermedades del esófago, estómago y duodeno (K20-K31)'
    elif codigo.startswith(('K40', 'K41', 'K42', 'K43', 'K44', 'K45', 'K46')):
        return 'Hernias abdominales (K40-K46)'
    elif codigo.startswith(('K50', 'K51', 'K52')):
        return 'Enteritis y colitis no infecciosas (K50-K52)'
    elif codigo.startswith(('K55', 'K56', 'K57', 'K58', 'K59', 'K60', 'K61', 'K62', 'K63')):
        return 'Otras enfermedades de los intestinos (K55-K63)'
    elif codigo.startswith(('K65', 'K66', 'K67')):
        return 'Enfermedades del peritoneo (K65-K67)'
    elif codigo.startswith(('K70', 'K71', 'K72', 'K73', 'K74', 'K75', 'K76', 'K77')):
        return 'Enfermedades del hígado (K70-K77)'
    elif codigo.startswith(('K80', 'K81', 'K82', 'K83', 'K84', 'K85', 'K86', 'K87')):
        return 'Trastornos de la vesícula biliar, tracto biliar y páncreas (K80-K87)'
    elif codigo.startswith(('K90', 'K91', 'K92', 'K93')):
        return 'Otras enfermedades del sistema digestivo (K90-K93)'
    elif codigo.startswith(('L00', 'L01', 'L02', 'L03', 'L04', 'L05', 'L06', 'L07', 'L08')):
        return 'Infecciones de la piel y el tejido subcutáneo (L00-L08)'
    elif codigo.startswith(('L10', 'L11', 'L12', 'L13', 'L14')):
        return 'Trastornos bullosos (L10-L14)'
    elif codigo.startswith(('L20', 'L21', 'L22', 'L23', 'L24', 'L25', 'L26', 'L27', 'L28', 'L29', 'L30')):
        return 'Dermatitis y eccema (L20-L30)'
    elif codigo.startswith(('L40', 'L41', 'L42', 'L43', 'L44', 'L45')):
        return 'Trastornos papuloescamosos (L40-L45)'
    elif codigo.startswith(('L50', 'L51', 'L52', 'L53', 'L54')):
        return 'Urticaria y eritema (L50-L54)'
    elif codigo.startswith(('L55', 'L56', 'L57', 'L58', 'L59')):
        return 'Trastornos cutáneos por radiación (L55-L59)'
    elif codigo.startswith(('L60', 'L61', 'L62', 'L63', 'L64', 'L65', 'L66', 'L67', 'L68', 'L69', 'L70', 'L71', 'L72', 'L73', 'L74', 'L75')):
        return 'Trastornos de las faneras (L60-L75)'
    elif codigo.startswith(('L80', 'L81', 'L82', 'L83', 'L84', 'L85', 'L86', 'L87', 'L88', 'L89', 'L90', 'L91', 'L92', 'L93', 'L94', 'L95', 'L96', 'L97', 'L98', 'L99')):
        return 'Otros trastornos de la piel y tejidos subcutáneos (L80-L99)'
    elif codigo.startswith(('M00', 'M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25')):
        return 'Artropatías (M00-M25)'
    elif codigo.startswith(('M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36')):
        return 'Trastornos sistémicos del tejido conectivo (M30-M36)'
    elif codigo.startswith(('M40', 'M41', 'M42', 'M43')):
        return 'Dorsopatías deformantes (M40-M43)'
    elif codigo.startswith(('M45', 'M46', 'M47', 'M48', 'M49')):
        return 'Espondiloartropatías (M45-M49)'
    elif codigo.startswith(('M50', 'M51', 'M52', 'M53', 'M54')):
        return 'Otras dorsopatías (M50-M54)'
    elif codigo.startswith(('M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79')):
        return 'Trastornos de los tejidos blandos (M60-M79)'
    elif codigo.startswith(('M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94')):
        return 'Osteopatías y condropatías (M80-M94)'
    elif codigo.startswith(('M95', 'M96', 'M97', 'M98', 'M99')):
        return 'Otros trastornos del sistema musculoesquelético y del tejido conectivo (M95-M99)'
    # Capítulo N: Sistema genitourinario
    elif codigo.startswith(('N00', 'N01', 'N02', 'N03', 'N04', 'N05', 'N06', 'N07', 'N08')):
        return 'Enfermedades glomerulares (N00-N08)'
    elif codigo.startswith(('N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16')):
        return 'Enfermedades renales tubulo-intersticiales (N10-N16)'
    elif codigo.startswith(('N17', 'N18', 'N19')):
        return 'Insuficiencia renal (N17-N19)'
    elif codigo.startswith(('N20', 'N21', 'N22', 'N23')):
        return 'Litiasis urinaria (N20-N23)'
    elif codigo.startswith(('N25', 'N26', 'N27', 'N28', 'N29')):
        return 'Otros trastornos del riñón y del uréter (N25-N29)'
    elif codigo.startswith(('N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39')):
        return 'Otras enfermedades del sistema urinario (N30-N39)'
    elif codigo.startswith(('N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51')):
        return 'Enfermedades de los órganos genitales masculinos (N40-N51)'
    elif codigo.startswith(('N60', 'N61', 'N62', 'N63', 'N64')):
        return 'Enfermedades de la mama (N60-N64)'
    elif codigo.startswith(('N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77')):
        return 'Enfermedades inflamatorias de los órganos pélvicos femeninos (N70-N77)'
    elif codigo.startswith(('N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98')):
        return 'Trastornos no inflamatorios de los órganos genitales femeninos (N80-N98)'
    elif codigo.startswith(('O00', 'O01', 'O02', 'O03', 'O04', 'O05', 'O06', 'O07', 'O08')):
        return 'Embarazo que termina en aborto (O00-O08)'
    elif codigo.startswith(('O10', 'O11', 'O12', 'O13', 'O14', 'O15', 'O16')):
        return 'Edema, proteinuria e hipertensión en el embarazo, parto y puerperio (O10-O16)'
    elif codigo.startswith(('O20', 'O21', 'O22', 'O23', 'O24', 'O25', 'O26', 'O27', 'O28', 'O29')):
        return 'Otras enfermedades de la madre que pueden afectar al feto (O20-O29)'
    elif codigo.startswith(('O30', 'O31', 'O32', 'O33', 'O34', 'O35', 'O36', 'O37', 'O38', 'O39', 'O40', 'O41', 'O42', 'O43', 'O44', 'O45', 'O46', 'O47', 'O48')):
        return 'Complicaciones del embarazo que requieren atención a la madre (O30-O48)'
    elif codigo.startswith(('O60', 'O61', 'O62', 'O63', 'O64', 'O65', 'O66', 'O67', 'O68', 'O69', 'O70', 'O71', 'O72', 'O73', 'O74', 'O75')):
        return 'Complicaciones del embarazo y el parto (O60-O75)'
    elif codigo.startswith(('O80', 'O81', 'O82', 'O83', 'O84')):
        return 'Parto (O80-O84)'
    elif codigo.startswith(('O85', 'O86', 'O87', 'O88', 'O89', 'O90', 'O91', 'O92')):
        return 'Enfermedades postparto (O85-O92)'
    elif codigo.startswith(('O95', 'O96', 'O97', 'O98', 'O99')):
        return 'Otras enfermedades relacionadas con el embarazo (O95-O99)'
    elif codigo.startswith(('P00', 'P01', 'P02', 'P03', 'P04')):
        return 'Afecciones de origen perinatal (P00-P04)'
    elif codigo.startswith(('P05', 'P06', 'P07', 'P08')):
        return 'Desórdenes relacionados con el embarazo (P05-P08)'
    elif codigo.startswith(('P10', 'P11', 'P12', 'P13', 'P14', 'P15')):
        return 'Traumatismo durante el parto (P10-P15)'
    elif codigo.startswith(('P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29')):
        return 'Enfermedades respiratorias y cardíacas durante el periodo perinatal (P20-P29)'
    elif codigo.startswith(('P35', 'P36', 'P37', 'P38', 'P39', 'P40')):
        return 'Enfermedades infecciosas del periodo perinatal (P35-P40)'
    elif codigo.startswith(('P50', 'P51', 'P52', 'P53', 'P54', 'P55', 'P56', 'P57', 'P58', 'P59', 'P60', 'P61')):
        return 'Enfermedades hematológicas y hemorrágicas del periodo perinatal (P50-P61)'
    elif codigo.startswith(('P70', 'P71', 'P72', 'P73', 'P74')):
        return 'Enfermedades endocrinas transitorias del recién nacido (P70-P74)'
    elif codigo.startswith(('P75', 'P76', 'P77', 'P78')):
        return 'Enfermedades del sistema digestivo del feto y del recién nacido (P75-P78)'
    elif codigo.startswith(('P90', 'P91', 'P92', 'P93', 'P94', 'P95', 'P96')):
        return 'Otras enfermedades del feto y del recién nacido (P90-P96)'

    # Capítulo R: Síntomas, signos y hallazgos anormales clínicos y de laboratorio
    elif codigo.startswith(('R00', 'R01', 'R02', 'R03', 'R04', 'R05', 'R06', 'R07', 'R08', 'R09')):
        return 'Síntomas que revelan una enfermedad circulatoria o respiratoria (R00-R09)'
    elif codigo.startswith(('R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19')):
        return 'Síntomas de enfermedades digestivas y desórdenes abdominales (R10-R19)'
    elif codigo.startswith(('R20', 'R21', 'R22', 'R23')):
        return 'Síntomas de enfermedades de la piel y del tejido subcutáneo (R20-R23)'
    elif codigo.startswith(('R25', 'R26', 'R27', 'R28', 'R29')):
        return 'Síntomas de enfermedades nerviosas y relacionadas con el sistema musculoesquelético (R25-R29)'
    elif codigo.startswith(('R30', 'R31', 'R32', 'R33', 'R34', 'R35', 'R36', 'R37', 'R38', 'R39')):
        return 'Síntomas de enfermedades urinarias (R30-R39)'
    elif codigo.startswith(('R40', 'R41', 'R42', 'R43', 'R44', 'R45', 'R46')):
        return 'Síntomas de enfermedades que afectan al comportamiento y al conocimiento (R40-R46)'
    elif codigo.startswith(('R47', 'R48', 'R49')):
        return 'Síntomas de enfermedades que afectan la voz y el habla (R47-R49)'
    elif codigo.startswith(('R50', 'R51', 'R52', 'R53', 'R54', 'R55', 'R56', 'R57', 'R58', 'R59', 'R60', 'R61', 'R62', 'R63', 'R64', 'R65', 'R66', 'R67', 'R68', 'R69')):
        return 'Síntomas generales (R50-R69)'
    elif codigo.startswith(('R70', 'R71', 'R72', 'R73', 'R74', 'R75', 'R76', 'R77', 'R78', 'R79')):
        return 'Valores anormales de los parámetros sanguíneos (R70-R79)'
    elif codigo.startswith(('R80', 'R81', 'R82')):
        return 'Valores anormales de los parámetros urinarios (R80-R82)'
    elif codigo.startswith(('R83', 'R84', 'R85', 'R86', 'R87', 'R88', 'R89')):
        return 'Valores anormales de otras pruebas clínicas (R83-R89)'
    elif codigo.startswith(('R90', 'R91', 'R92', 'R93', 'R94')):
        return 'Hallazgos anormales en el diagnóstico por imagen (R90-R94)'
    elif codigo.startswith(('R95', 'R96', 'R97', 'R98', 'R99')):
        return 'Causas de muerte (R95-R99)'
    elif codigo.startswith(('S00', 'S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09')):
        return 'Traumatismos de la cabeza (S00-S09)'
    elif codigo.startswith(('S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19')):
        return 'Traumatismos de cuello (S10-S19)'
    elif codigo.startswith(('S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29')):
        return 'Traumatismos de tórax (S20-S29)'
    elif codigo.startswith(('S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39')):
        return 'Traumatismo del abdomen, área lumbosacra y pelvis (S30-S39)'
    elif codigo.startswith(('S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47', 'S48', 'S49')):
        return 'Traumatismos de los hombros y brazos (S40-S49)'
    elif codigo.startswith(('S50', 'S51', 'S52', 'S53', 'S54', 'S55', 'S56', 'S57', 'S58', 'S59')):
        return 'Traumatismos del codo y del antebrazo (S50-S59)'
    elif codigo.startswith(('S60', 'S61', 'S62', 'S63', 'S64', 'S65', 'S66', 'S67', 'S68', 'S69')):
        return 'Traumatismos en muñecas y manos (S60-S69)'
    elif codigo.startswith(('S70', 'S71', 'S72', 'S73', 'S74', 'S75', 'S76', 'S77', 'S78', 'S79')):
        return 'Traumatismos en caderas y muslos (S70-S79)'
    elif codigo.startswith(('S80', 'S81', 'S82', 'S83', 'S84', 'S85', 'S86', 'S87', 'S88', 'S89')):
        return 'Traumatismos en rodillas y piernas (S80-S89)'
    elif codigo.startswith(('S90', 'S91', 'S92', 'S93', 'S94', 'S95', 'S96', 'S97', 'S98', 'S99')):
        return 'Traumatismos en tobillos y pies (S90-S99)'
    elif codigo.startswith(('T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07')):
        return 'Lesiones múltiples (T00-T07)'
    elif codigo.startswith(('T08', 'T09', 'T10', 'T11', 'T12', 'T13', 'T14')):
        return 'Lesiones no clasificadas en cabeza, cuello y otras partes (T08-T14)'
    elif codigo.startswith(('T15', 'T16', 'T17', 'T18', 'T19')):
        return 'Cuerpos extraños en alguna parte del cuerpo (T15-T19)'
    elif codigo.startswith(('T20', 'T21', 'T22', 'T23', 'T24', 'T25', 'T26', 'T27', 'T28', 'T29', 'T30', 'T31', 'T32')):
        return 'Quemaduras y corrosiones (T20-T32)'
    elif codigo.startswith(('T33', 'T34', 'T35')):
        return 'Congelaciones (T33-T35)'
    elif codigo.startswith(('T36', 'T37', 'T38', 'T39', 'T40', 'T41', 'T42', 'T43', 'T44', 'T45', 'T46', 'T47', 'T48', 'T49', 'T50')):
        return 'Intoxicaciones por fármacos (T36-T50)'
    elif codigo.startswith(('T51', 'T52', 'T53', 'T54', 'T55', 'T56', 'T57', 'T58', 'T59', 'T60', 'T61', 'T62', 'T63', 'T64', 'T65')):
        return 'Intoxicaciones por sustancias no medicinales (T51-T65)'
    elif codigo.startswith(('T66', 'T67', 'T68', 'T69', 'T70', 'T71', 'T72', 'T73', 'T74', 'T75', 'T76', 'T77', 'T78')):
        return 'Lesiones por otras causas externas (T66-T78)'
    elif codigo.startswith(('T79',)):
        return 'Complicaciones traumáticas (T79)'
    elif codigo.startswith(('T80', 'T81', 'T82', 'T83', 'T84', 'T85', 'T86', 'T87', 'T88')):
        return 'Complicaciones quirúrgicas (T80-T88)'
    elif codigo.startswith(('T90', 'T91', 'T92', 'T93', 'T94', 'T95', 'T96', 'T97', 'T98', 'T99')):
        return 'Complicaciones post-traumáticas no clasificadas en otra parte (T90-T99)'
    elif codigo.startswith(tuple(f'V{str(i).zfill(2)}' for i in range(0, 99))):
        return 'Accidentes de transporte (V00-V98)'
    elif codigo.startswith(tuple(f'W{str(i).zfill(2)}' for i in range(0, 60))):
        return 'Caídas y accidentes diversos (W00-X59)'
    elif codigo.startswith(tuple(f'X{str(i).zfill(2)}' for i in range(60))):
        return 'Otras causas externas de mortalidad (X60-Y36)'
    elif codigo.startswith(tuple(f'Y{str(i).zfill(2)}' for i in range(40, 99))):
        return 'Efectos secundarios de tratamientos (Y40-Y98)'

    # Capítulo Z: Factores que influyen en el estado de salud
    elif codigo.startswith(('Z00', 'Z01', 'Z02', 'Z03', 'Z04', 'Z05', 'Z06', 'Z07', 'Z08', 'Z09', 'Z10', 'Z11', 'Z12', 'Z13')):
        return 'Pruebas para aclarar o investigar problemas de salud (Z00-Z13)'
    elif codigo.startswith(('Z20', 'Z21', 'Z22', 'Z23', 'Z24', 'Z25', 'Z26', 'Z27', 'Z28', 'Z29')):
        return 'Contactos y exposición a enfermedades contagiosas (Z20-Z29)'
    elif codigo.startswith(('Z30', 'Z31', 'Z32', 'Z33', 'Z34', 'Z35', 'Z36', 'Z37', 'Z38', 'Z39')):
        return 'Intervenciones relativas a la reproducción (Z30-Z39)'
    elif codigo.startswith(('Z40', 'Z41', 'Z42', 'Z43', 'Z44', 'Z45', 'Z46', 'Z47', 'Z48', 'Z49', 'Z50', 'Z51', 'Z52', 'Z53', 'Z54')):
        return 'Personas candidatas a cirugía (Z40-Z54)'
    elif codigo.startswith(('Z55', 'Z56', 'Z57', 'Z58', 'Z59', 'Z60', 'Z61', 'Z62', 'Z63', 'Z64', 'Z65')):
        return 'Personas con problemas potenciales psíquicos o psicosociales (Z55-Z65)'
    elif codigo.startswith(('Z70', 'Z71', 'Z72', 'Z73', 'Z74', 'Z75', 'Z76')):
        return 'Consultas (Z70-Z76)'
    elif codigo.startswith(('Z80', 'Z81', 'Z82', 'Z83', 'Z84', 'Z85', 'Z86', 'Z87', 'Z88', 'Z89', 'Z90', 'Z91', 'Z92', 'Z93', 'Z94', 'Z95', 'Z96', 'Z97', 'Z98', 'Z99')):
        return 'Historias (Z80-Z99)'

    # Capítulo U: Códigos de uso provisional
    elif codigo.startswith(('U00', 'U01', 'U02', 'U03', 'U04', 'U05', 'U06', 'U08', 'U09', 'U10', 'U11', 'U12', 'U13', 'U14', 'U15', 'U16', 'U17', 'U18', 'U19', 'U20', 'U21', 'U22', 'U23', 'U24', 'U25', 'U26', 'U27', 'U28', 'U29', 'U30', 'U31', 'U32', 'U33', 'U34', 'U35', 'U36', 'U37', 'U38', 'U39', 'U40', 'U41', 'U42', 'U43', 'U44', 'U45', 'U46', 'U47', 'U48', 'U49')):
        return 'Asignación provisional de nuevas enfermedades de etiología incierta (U00-U49)'
    elif codigo.startswith(('U07',)):
        return 'Códigos para uso de emergencia (U07)'
    elif codigo.startswith(('U80', 'U81', 'U82', 'U83', 'U84', 'U85', 'U86', 'U87', 'U88', 'U89')):
        return 'Agentes bacterianos resistentes a los antibióticos (U80-U89)'


    return None
