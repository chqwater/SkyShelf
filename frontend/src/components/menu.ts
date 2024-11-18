import { Menus } from '../types/menu';

export const menuData: Menus[] = [
    {
        id: '0',
        title: 'Current Reading',
        index: '/home/booklist',
        icon: 'Reading',
    },
    {
        id: '1',
        title: 'Recommendation',
        index: '/home/recommendation',
        icon: 'HomeFilled'
    }
];

export const menuAdmin: Menus[] = [
    {
        id: '0',
        title: 'Book Management',
        index: '/admin/book',
        icon: 'Management'
    },
    {
        id: '1',
        title: 'User Management',
        index: '/admin/user',
        icon: 'UserFilled'
    }
]