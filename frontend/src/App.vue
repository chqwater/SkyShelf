<template>
	<router-view />
</template>

<script setup lang="ts">
import { useThemeStore } from './store/theme';

const theme = useThemeStore();
theme.initTheme();
</script>
<style>
</style>
