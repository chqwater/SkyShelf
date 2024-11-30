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
