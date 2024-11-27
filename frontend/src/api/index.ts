import request from '../utils/request';


export function userRegistration(data: any) {
    return request({
        url: '/api/register',
        method: 'post',
        data
    })
}

export function updateJourney(data :any) {
    return request({
        url: 'api/update-journey',
        method: 'post',
        data
    })
}
