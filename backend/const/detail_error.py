## invalid 
## Age invalie 
## card 
CODE_VALID = 0 
CODE_UNAUTHORIZED = 404 
CODE_INVALID_AGE = 422
CODE_INVALID_TYPE = 423
CODE_USER_EXISTS = 424
CODE_DONT_HAVE_PERMISSIONS = 425
CODE_RECORD_NOT_FOUND = 426
CODE_CANNOT_CREATE = 427
CODE_CANNOT_DELETE = 428
CODE_CANNOT_UPDATE = 429
CODE_CANNOT_GET = 430
CODE_ERROR_COMOM = 555 
CODE_INVALID_YEAR_PUBLICATION = 431 
CODE_INVALID_CATEGORY_BOOK = 432 
CODE_INVALID_NUMBER_BOOKS_CAN_BE_BORROW = 433
CODE_ENTITY_EXISTS = 434 



DETAIL_DATA_VALID = "Valid"
DETAIL_INVALID_AGE= "Age is invalid"
DETAIL_INVALID_TYPE= "Type is invalid"
DETAIL_UNAUTHORIZED = "May be unauthorized"
CODE_USER_EXISTS = "Info is duplicate or database error, try again"
DETAIL_DONT_HAVE_PERMISSIONS = "User does not have this permissions"
DETAIL_RECORD_NOT_FOUND = "Record not found"
DETAIL_CANNOT_CREATE = "Can not create entity"
DETAIL_CANNOT_DELETE = "Can not delete entity"
DETAIL_CANNOT_UPDATE = "Can not update entity"
DETAIL_CANNOT_GET = "Can not get entity"
DETAIl_ERROR_COMON = "Some thing went wrong"
DETAIL_INVALID_YEAR_PUBLICATION = "Year of publication not valid"
DETAIL_INVALID_CATEGORY_BOOK = "Category invalid"
DETAIL_INVALID_NUMBER_BOOKS_CAN_BE_BORROW = "Numbers'book must be less than or equal to rule"
DETAIL_ENTITY_EXISTS = "Entity is already exists"





map_err = {
    CODE_VALID: DETAIL_DATA_VALID, 
    CODE_INVALID_AGE: DETAIL_INVALID_AGE, 
    CODE_INVALID_TYPE: DETAIL_INVALID_TYPE, 
    CODE_UNAUTHORIZED: DETAIL_UNAUTHORIZED, 
    CODE_USER_EXISTS: CODE_USER_EXISTS,
    CODE_DONT_HAVE_PERMISSIONS: DETAIL_DONT_HAVE_PERMISSIONS,
    CODE_RECORD_NOT_FOUND: DETAIL_RECORD_NOT_FOUND, 
    CODE_CANNOT_CREATE: DETAIL_CANNOT_CREATE , 
    CODE_CANNOT_DELETE: DETAIL_CANNOT_DELETE, 
    CODE_CANNOT_UPDATE: DETAIL_CANNOT_UPDATE, 
    CODE_CANNOT_GET: DETAIL_CANNOT_GET, 
    CODE_ERROR_COMOM: DETAIl_ERROR_COMON, 
    CODE_INVALID_YEAR_PUBLICATION: DETAIL_INVALID_YEAR_PUBLICATION,
    CODE_INVALID_CATEGORY_BOOK: DETAIL_INVALID_CATEGORY_BOOK,
    CODE_INVALID_NUMBER_BOOKS_CAN_BE_BORROW: DETAIL_INVALID_NUMBER_BOOKS_CAN_BE_BORROW, 
    CODE_ENTITY_EXISTS: DETAIL_ENTITY_EXISTS
}

