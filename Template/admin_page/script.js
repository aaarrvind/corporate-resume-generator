document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebarOverlay');
    const menuBtn = document.getElementById('menuBtn');
    const closeSidebarBtn = document.getElementById('closeSidebarBtn');
    const paginationBtns = document.querySelectorAll('.pagination-btn');
    
    // Mobile sidebar toggle
    function openSidebar() {
      sidebar.classList.add('open');
      sidebarOverlay.classList.add('show');
      document.body.style.overflow = 'hidden';
    }
    
    function closeSidebar() {
      sidebar.classList.remove('open');
      sidebarOverlay.classList.remove('show');
      document.body.style.overflow = '';
    }
    
    menuBtn.addEventListener('click', openSidebar);
    closeSidebarBtn.addEventListener('click', closeSidebar);
    sidebarOverlay.addEventListener('click', closeSidebar);
    
    // Navigation active state
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
      item.addEventListener('click', function(e) {
        // If on mobile, close the sidebar
        if (window.innerWidth < 768) {
          closeSidebar();
        }
        
        // Remove active class from all items
        navItems.forEach(navItem => {
          navItem.classList.remove('active');
        });
        
        // Add active class to clicked item
        this.classList.add('active');
      });
    });
    
    // Pagination
    paginationBtns.forEach(btn => {
      if (!btn.classList.contains('disabled') && !btn.disabled) {
        btn.addEventListener('click', function() {
          // Remove active class from all pagination buttons
          paginationBtns.forEach(paginationBtn => {
            paginationBtn.classList.remove('active');
          });
          
          // Add active class to clicked button if it's a number
          if (!this.querySelector('.icon')) {
            this.classList.add('active');
          }
        });
      }
    });
    
    // Responsive behavior
    function handleResize() {
      if (window.innerWidth >= 768) {
        closeSidebar();
        sidebar.style.transform = '';
      }
    }
    
    window.addEventListener('resize', handleResize);
    
    // Table sorting (placeholder functionality)
    const sortButton = document.querySelector('.sort-button');
    sortButton.addEventListener('click', function() {
      // This would typically trigger a sort function
      alert('Sort functionality would be implemented here');
    });
    
    // Search functionality (placeholder)
    const searchInputs = document.querySelectorAll('.search-input');
    searchInputs.forEach(input => {
      input.addEventListener('input', function() {
        // This would typically filter the table or trigger a search
        console.log('Searching for:', this.value);
      });
    });
  });