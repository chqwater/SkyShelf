import request from '../utils/request';


export function userRegistration(data: any) {
    return request({
        url: '/api/register',
        method: 'post',
        data
    })
}

export function userLogin(data:any){
    return request({
        url: '/api/login',
        method: 'post',
        data
    })
}

export function updateJourney(data :any) {
    return request({
        url: '/api/update-journey',
        method: 'post',
        data
    })
}

export function updatePassword(data:any){
    return request({
        url: '/api/new-password',
        method: 'post',
        data
    })
}

export function addBook(data:any){
    return request({
        url: '/api/add_book',
        method: 'post',
        data
    })
}

export function saveProgress(data:any){
    return request({
        url: '/api/reading_progress',
        method: 'post',
        data
    })
}

export function getRecommendation(id:any) {
    return request({
        url: `/api/recommendation/${id}`,
        method: 'get'
    });
}

export function getShelf(id:any){
    return request({
        url: `/api/shelf/${id}`,
        method: 'get'
    })
}

export function getAllUserInfo(){
    return request({
        url: 'api/admin/users',
        method: 'get'
    })
}

export function getBooks(category_id = null) {
    const query = category_id ? `?category_id=${category_id}` : '';
    return request({
        url: `api/admin/books${query}`,
        method: 'GET'
    });
}

export function editBook(data: any){
    return request({
        url: 'api/admin/edit-book',
        method: 'post',
        data
    })
}

export function deleteBook(book_id: number) {
    const query = book_id ? `?book_id=${book_id}` : '';
    return request({
        url: `api/admin/delete-book${query}`,
        method: 'post' // Sending the book_id as part of the payload
    })
}

export function createBook(data:any){
    return request({
        url: 'api/admin/create-book',
        method: 'post',
        data
    })
}
