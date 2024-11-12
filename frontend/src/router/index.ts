import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import { usePermissStore } from '../store/permiss';
import Home from '../views/home.vue';
import NProgress from 'nprogress';
import 'nprogress/nprogress.css';
import AdminHome from '@/views/admin/adminHome.vue';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/home',
    },
    {
        path: '/home',
        name: 'Home',
        component: Home,
        children: [
            {
                path: 'dashboard',
                name: 'dashboard',
                meta: {
                    title: 'Current Reading',
                    noAuth: true,
                },
                component: () => import('../views/dashboard.vue'),
            },
            {
				path: 'recommendation',
				name: 'recommendation',
				meta: {
					title: 'Recommendation',
					noAuth: true,
				},
				component: () => import('../views/recommendation.vue')
            },
            {
                path: 'ucenter',
                name: 'ucenter',
                meta: {
                    title: 'Profile',
                },
                component: () => import('../views/pages/ucenter.vue'),
            }
        ],
    },
    {
        path: '/admin',
        name: 'Admin',
        component: AdminHome,
        children: [
            {
                path: 'book',
                name: 'book',
                meta: {
                    title: 'Book-Admin',
                    noAuth: true
                },
                component: () => import('../views/admin/bookAdmin.vue')
            },
            {
                path: 'user',
                name: 'user',
                meta: {
                    title: 'User-Admin',
                    noAuth: true
                },
                component: () => import('../views/admin/userAdmin.vue')
            }
        ]
    },
    {
        path: '/login',
        meta: {
            title: 'Login',
            noAuth: true,
        },
        component: () => import(/* webpackChunkName: "login" */ '../views/pages/login.vue'),
    },
    {
        path: '/register',
        meta: {
            title: 'Register',
            noAuth: true,
        },
        component: () => import(/* webpackChunkName: "register" */ '../views/pages/register.vue'),
    },
    {
        path: '/journey',
        meta: {
            title: 'Journey',
            noAuth: true
        },
        component: () => import(/* webpackChunkName: "register" */ '../views/pages/journey.vue'),
    },
    {
        path: '/reset-pwd',
        meta: {
            title: 'Reset password',
            noAuth: true,
        },
        component: () => import(/* webpackChunkName: "reset-pwd" */ '../views/pages/reset-pwd.vue'),
    },
    {
        path: '/403',
        meta: {
            title: 'Not authorized',
            noAuth: true,
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/pages/403.vue'),
    },
    {
        path: '/404',
        meta: {
            title: 'Page not found',
            noAuth: true,
        },
        component: () => import(/* webpackChunkName: "404" */ '../views/pages/404.vue'),
    },
    { path: '/:path(.*)', redirect: '/404' },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    NProgress.start();
    const role = localStorage.getItem('vuems_name');
    const permiss = usePermissStore();

    if (!role && to.meta.noAuth !== true) {
        next('/login');
    } else if (typeof to.meta.permiss == 'string' && !permiss.key.includes(to.meta.permiss)) {
        next('/403');
    } else {
        next();
    }
});

router.afterEach(() => {
    NProgress.done();
});

export default router;
