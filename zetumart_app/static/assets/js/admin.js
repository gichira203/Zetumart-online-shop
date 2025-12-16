// ZetuMart Admin Dashboard JavaScript
class ZetuMartAdmin {
  constructor() {
    this.currentSection = 'dashboard';
    this.data = {
      products: [],
      orders: [],
      users: [],
      messages: []
    };
    this.init();
  }

  init() {
    this.setupNavigation();
    this.setupEventListeners();
    this.loadDashboardData();
    this.initChart();
  }

  setupNavigation() {
    // Sidebar navigation
    const navItems = document.querySelectorAll('#sidebarMenu .list-group-item');
    navItems.forEach(item => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        const text = item.querySelector('span').textContent.toLowerCase();
        this.showSection(text);
        
        // Update active state
        navItems.forEach(nav => nav.classList.remove('active'));
        item.classList.add('active');
      });
    });
  }

  showSection(section) {
    // Hide all sections
    document.querySelectorAll('.admin-section').forEach(sec => {
      sec.style.display = 'none';
    });

    // Show selected section
    switch(section) {
      case 'main dashboard':
        document.getElementById('dashboardSection').style.display = 'block';
        this.loadDashboardData();
        break;
      case 'orders':
        document.getElementById('ordersSection').style.display = 'block';
        this.loadOrders();
        break;
      case 'users':
        document.getElementById('usersSection').style.display = 'block';
        this.loadUsers();
        break;
      case 'password':
        document.getElementById('passwordSection').style.display = 'block';
        break;
      case 'add admin':
        document.getElementById('addAdminSection').style.display = 'block';
        break;
      case 'add products':
        document.getElementById('productsSection').style.display = 'block';
        this.loadProducts();
        break;
      case 'messages':
        document.getElementById('messagesSection').style.display = 'block';
        this.loadMessages();
        break;
      default:
        document.getElementById('dashboardSection').style.display = 'block';
    }
  }

  setupEventListeners() {
    // Password change form
    const passwordForm = document.getElementById('passwordChangeForm');
    if (passwordForm) {
      passwordForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.changePassword();
      });
    }

    // Add admin form
    const adminForm = document.getElementById('addAdminForm');
    if (adminForm) {
      adminForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.addAdmin();
      });
    }

    // Product form submission
    const productForm = document.getElementById('addProductForm');
    if (productForm) {
      productForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.addProduct();
      });
    }

    // Multiple image preview handlers
    for (let i = 1; i <= 4; i++) {
      const imageInput = document.getElementById(`productImage${i}`);
      if (imageInput) {
        imageInput.addEventListener('change', (e) => {
          this.previewImage(e.target.files[0], i);
        });
      }
    }

    // Product search
    const productSearch = document.getElementById('productSearch');
    if (productSearch) {
      productSearch.addEventListener('input', (e) => {
        this.searchProducts(e.target.value);
      });
    }

    // Logout
    const logoutBtn = document.querySelector('[href*="logout"]');
    if (logoutBtn) {
      logoutBtn.addEventListener('click', (e) => {
        e.preventDefault();
        this.logout();
      });
    }
  }

  async loadDashboardData() {
    try {
      // Load data from localStorage or API
      this.data.products = this.getFromStorage('products') || this.generateMockProducts();
      this.data.orders = this.getFromStorage('orders') || this.generateMockOrders();
      this.data.users = this.getFromStorage('users') || this.generateMockUsers();
      this.data.messages = this.getFromStorage('messages') || this.generateMockMessages();

      // Update dashboard counters
      document.getElementById('totalProducts').textContent = this.data.products.length;
      document.getElementById('totalOrders').textContent = this.data.orders.length;
      document.getElementById('totalUsers').textContent = this.data.users.length;
      document.getElementById('totalMessages').textContent = this.data.messages.length;

      // Load recent orders
      this.loadRecentOrders();
      
      // Update chart
      this.updateChart();
    } catch (error) {
      console.error('Error loading dashboard data:', error);
    }
  }

  loadRecentOrders() {
    const tbody = document.getElementById('recentOrdersTable');
    if (!tbody) return;

    const recentOrders = this.data.orders.slice(0, 5);
    tbody.innerHTML = '';

    recentOrders.forEach(order => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>#${order.id}</td>
        <td>${order.customer}</td>
        <td>KSh ${order.total.toLocaleString()}</td>
        <td><span class="badge bg-${this.getStatusColor(order.status)}">${order.status}</span></td>
        <td>${new Date(order.date).toLocaleDateString()}</td>
        <td>
          <button class="btn btn-sm btn-outline-primary" onclick="admin.showOrderDetails(${order.id})">
            <i class="fas fa-eye"></i>
          </button>
        </td>
      `;
      tbody.appendChild(row);
    });
  }

  loadOrders() {
    const tbody = document.getElementById('ordersTable');
    if (!tbody) return;

    tbody.innerHTML = '<tr><td colspan="8" class="text-center">Loading orders...</td></tr>';

    setTimeout(() => {
      tbody.innerHTML = '';
      this.data.orders.forEach(order => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>#${order.id}</td>
          <td>${order.customer}</td>
          <td>${order.items.length} items</td>
          <td>KSh ${order.total.toLocaleString()}</td>
          <td>${order.payment}</td>
          <td>
            <select class="form-select form-select-sm" onchange="admin.updateOrderStatus(${order.id}, this.value)">
              <option value="pending" ${order.status === 'pending' ? 'selected' : ''}>Pending</option>
              <option value="processing" ${order.status === 'processing' ? 'selected' : ''}>Processing</option>
              <option value="shipped" ${order.status === 'shipped' ? 'selected' : ''}>Shipped</option>
              <option value="delivered" ${order.status === 'delivered' ? 'selected' : ''}>Delivered</option>
              <option value="cancelled" ${order.status === 'cancelled' ? 'selected' : ''}>Cancelled</option>
            </select>
          </td>
          <td>${new Date(order.date).toLocaleDateString()}</td>
          <td>
            <button class="btn btn-sm btn-outline-primary" onclick="admin.showOrderDetails(${order.id})">
              <i class="fas fa-eye"></i>
            </button>
          </td>
        `;
        tbody.appendChild(row);
      });
    }, 500);
  }

  loadUsers() {
    const tbody = document.getElementById('usersTable');
    if (!tbody) return;

    tbody.innerHTML = '<tr><td colspan="8" class="text-center">Loading users...</td></tr>';

    setTimeout(() => {
      tbody.innerHTML = '';
      this.data.users.forEach(user => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${user.id}</td>
          <td>${user.username}</td>
          <td>${user.email}</td>
          <td>${user.fullName}</td>
          <td>${user.phone}</td>
          <td>${user.county}</td>
          <td>${new Date(user.joined).toLocaleDateString()}</td>
          <td>
            <button class="btn btn-sm btn-outline-info" onclick="admin.viewUserDetails(${user.id})">
              <i class="fas fa-eye"></i>
            </button>
            <button class="btn btn-sm btn-outline-danger" onclick="admin.deleteUser(${user.id})">
              <i class="fas fa-trash"></i>
            </button>
          </td>
        `;
        tbody.appendChild(row);
      });
    }, 500);
  }

  loadProducts() {
    const tbody = document.getElementById('productsTable');
    if (!tbody) return;

    tbody.innerHTML = '<tr><td colspan="7" class="text-center">Loading products...</td></tr>';

    setTimeout(() => {
      this.renderProducts(this.data.products);
    }, 500);
  }

  renderProducts(products) {
    const tbody = document.getElementById('productsTable');
    if (!tbody) return;

    tbody.innerHTML = '';
    products.forEach(product => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td><img src="${product.image}" alt="${product.name}" style="width: 50px; height: 50px; object-fit: cover;"></td>
        <td>${product.name}</td>
        <td>${product.category}</td>
        <td>KSh ${product.price.toLocaleString()}</td>
        <td>${product.stock}</td>
        <td><span class="badge bg-${product.stock > 0 ? 'success' : 'danger'}">${product.stock > 0 ? 'Available' : 'Out of Stock'}</span></td>
        <td>
          <button class="btn btn-sm btn-outline-primary" onclick="admin.editProduct(${product.id})">
            <i class="fas fa-edit"></i>
          </button>
          <button class="btn btn-sm btn-outline-danger" onclick="admin.deleteProduct(${product.id})">
            <i class="fas fa-trash"></i>
          </button>
        </td>
      `;
      tbody.appendChild(row);
    });
  }

  loadMessages() {
    const tbody = document.getElementById('messagesTable');
    if (!tbody) return;

    tbody.innerHTML = '<tr><td colspan="8" class="text-center">Loading messages...</td></tr>';

    setTimeout(() => {
      tbody.innerHTML = '';
      this.data.messages.forEach(message => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${message.id}</td>
          <td>${message.name}</td>
          <td>${message.email}</td>
          <td>${message.subject}</td>
          <td>${message.message.substring(0, 50)}...</td>
          <td>${new Date(message.date).toLocaleDateString()}</td>
          <td><span class="badge bg-${message.read ? 'secondary' : 'primary'}">${message.read ? 'Read' : 'New'}</span></td>
          <td>
            <button class="btn btn-sm btn-outline-primary" onclick="admin.viewMessage(${message.id})">
              <i class="fas fa-eye"></i>
            </button>
            <button class="btn btn-sm btn-outline-success" onclick="admin.replyToMessage(${message.id})">
              <i class="fas fa-reply"></i>
            </button>
            <button class="btn btn-sm btn-outline-danger" onclick="admin.deleteMessage(${message.id})">
              <i class="fas fa-trash"></i>
            </button>
          </td>
        `;
        tbody.appendChild(row);
      });
    }, 500);
  }

  // Message Management Functions
  viewMessage(id) {
    const message = this.data.messages.find(m => m.id === id);
    if (!message) return;

    // Mark as read
    message.read = true;
    this.saveToStorage('messages', this.data.messages);

    // Show message modal
    const modalHtml = `
      <div class="modal fade" id="messageModal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Message Details</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <p><strong>From:</strong> ${message.name} (${message.email})</p>
              <p><strong>Subject:</strong> ${message.subject}</p>
              <p><strong>Date:</strong> ${new Date(message.date).toLocaleString()}</p>
              <hr>
              <p>${message.message}</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary" onclick="admin.replyToMessage(${message.id})">Reply</button>
            </div>
          </div>
        </div>
      </div>
    `;

    // Remove existing modal
    const existingModal = document.getElementById('messageModal');
    if (existingModal) existingModal.remove();

    // Add new modal
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    const modal = new bootstrap.Modal(document.getElementById('messageModal'));
    modal.show();
  }

  replyToMessage(id) {
    const message = this.data.messages.find(m => m.id === id);
    if (!message) return;

    const modalHtml = `
      <div class="modal fade" id="replyModal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Reply to Message</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label class="form-label">To:</label>
                <input type="email" class="form-control" value="${message.email}" readonly>
              </div>
              <div class="mb-3">
                <label class="form-label">Subject:</label>
                <input type="text" class="form-control" value="Re: ${message.subject}" readonly>
              </div>
              <div class="mb-3">
                <label class="form-label">Reply Message:</label>
                <textarea class="form-control" id="replyMessage" rows="5" placeholder="Type your reply here..."></textarea>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
              <button type="button" class="btn btn-primary" onclick="admin.sendReply(${message.id})">Send Reply</button>
            </div>
          </div>
        </div>
      </div>
    `;

    // Remove existing modal
    const existingModal = document.getElementById('replyModal');
    if (existingModal) existingModal.remove();

    // Add new modal
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    const modal = new bootstrap.Modal(document.getElementById('replyModal'));
    modal.show();
  }

  sendReply(messageId) {
    const replyText = document.getElementById('replyMessage').value;
    if (!replyText.trim()) {
      alert('Please enter a reply message');
      return;
    }

    // In a real application, this would send an email
    // For now, we'll just show a success message
    alert('Reply sent successfully!');
    
    // Close modal
    const modal = bootstrap.Modal.getInstance(document.getElementById('replyModal'));
    modal.hide();
  }

  deleteMessage(id) {
    if (confirm('Are you sure you want to delete this message?')) {
      this.data.messages = this.data.messages.filter(m => m.id !== id);
      this.saveToStorage('messages', this.data.messages);
      this.loadMessages();
      this.showAlert('Message deleted successfully', 'success');
    }
  }

  // Order Management Functions
  showOrderDetails(id) {
    const order = this.data.orders.find(o => o.id === id);
    if (!order) return;

    const modalHtml = `
      <div class="modal fade" id="orderDetailsModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Order Details - #${order.id}</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <div class="row mb-3">
                <div class="col-md-6">
                  <p><strong>Customer:</strong> ${order.customer}</p>
                  <p><strong>Email:</strong> ${order.email}</p>
                  <p><strong>Phone:</strong> ${order.phone}</p>
                  <p><strong>County:</strong> ${order.county}</p>
                </div>
                <div class="col-md-6">
                  <p><strong>Order Date:</strong> ${new Date(order.date).toLocaleString()}</p>
                  <p><strong>Payment:</strong> ${order.payment}</p>
                  <p><strong>Status:</strong> <span class="badge bg-${this.getStatusColor(order.status)}">${order.status}</span></p>
                  <p><strong>Total:</strong> KSh ${order.total.toLocaleString()}</p>
                </div>
              </div>
              <h6>Order Items:</h6>
              <div class="table-responsive">
                <table class="table table-sm">
                  <thead>
                    <tr>
                      <th>Product</th>
                      <th>Price</th>
                      <th>Quantity</th>
                      <th>Subtotal</th>
                    </tr>
                  </thead>
                  <tbody>
                    ${order.items.map(item => `
                      <tr>
                        <td>${item.name}</td>
                        <td>KSh ${item.price.toLocaleString()}</td>
                        <td>${item.quantity}</td>
                        <td>KSh ${(item.price * item.quantity).toLocaleString()}</td>
                      </tr>
                    `).join('')}
                  </tbody>
                  <tfoot>
                    <tr>
                      <th colspan="3">Total:</th>
                      <th>KSh ${order.total.toLocaleString()}</th>
                    </tr>
                  </tfoot>
                </table>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    `;

    // Remove existing modal
    const existingModal = document.getElementById('orderDetailsModal');
    if (existingModal) existingModal.remove();

    // Add new modal
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    const modal = new bootstrap.Modal(document.getElementById('orderDetailsModal'));
    modal.show();
  }

  updateOrderStatus(id, newStatus) {
    const order = this.data.orders.find(o => o.id === id);
    if (order) {
      order.status = newStatus;
      this.saveToStorage('orders', this.data.orders);
      this.showAlert('Order status updated successfully', 'success');
    }
  }

  // User Management Functions
  viewUserDetails(id) {
    const user = this.data.users.find(u => u.id === id);
    if (!user) return;

    const modalHtml = `
      <div class="modal fade" id="userDetailsModal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">User Details</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <p><strong>User ID:</strong> ${user.id}</p>
              <p><strong>Username:</strong> ${user.username}</p>
              <p><strong>Email:</strong> ${user.email}</p>
              <p><strong>Full Name:</strong> ${user.fullName}</p>
              <p><strong>Phone:</strong> ${user.phone}</p>
              <p><strong>County:</strong> ${user.county}</p>
              <p><strong>Address:</strong> ${user.address}</p>
              <p><strong>Joined:</strong> ${new Date(user.joined).toLocaleString()}</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    `;

    // Remove existing modal
    const existingModal = document.getElementById('userDetailsModal');
    if (existingModal) existingModal.remove();

    // Add new modal
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    const modal = new bootstrap.Modal(document.getElementById('userDetailsModal'));
    modal.show();
  }

  deleteUser(id) {
    if (confirm('Are you sure you want to delete this user? This action cannot be undone.')) {
      this.data.users = this.data.users.filter(u => u.id !== id);
      this.saveToStorage('users', this.data.users);
      this.loadUsers();
      this.showAlert('User deleted successfully', 'success');
    }
  }

  // Product Management Functions
  async addProduct() {
    const form = document.getElementById('addProductForm');
    const formData = new FormData(form);
    const submitBtn = document.getElementById('submitProductBtn');
    
    // Disable submit button and show loading
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Adding Product...';
    
    try {
      const response = await fetch('/api/admin/products/', {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        }
      });
      
      if (response.ok) {
        const result = await response.json();
        this.showAlert('Product added successfully!', 'success');
        form.reset();
        
        // Clear image previews
        for (let i = 1; i <= 4; i++) {
          const preview = document.getElementById(`imagePreview${i}`);
          if (preview) preview.innerHTML = '';
        }
        
        // Close modal
        const modal = bootstrap.Modal.getInstance(document.getElementById('addProductModal'));
        modal.hide();
        
        // Reload products
        this.loadProducts();
      } else {
        const error = await response.json();
        this.showAlert('Error adding product: ' + (error.error || 'Unknown error'), 'error');
      }
    } catch (error) {
      console.error('Error:', error);
      this.showAlert('Error adding product. Please try again.', 'error');
    } finally {
      // Re-enable submit button
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="fas fa-plus"></i> Add Product';
    }
  }

  editProduct(id) {
    const product = this.data.products.find(p => p.id === id);
    if (!product) return;

    // Populate edit form
    document.getElementById('editProductId').value = product.id;
    document.getElementById('editProductName').value = product.name;
    document.getElementById('editProductCategory').value = product.category;
    document.getElementById('editProductPrice').value = product.price;
    document.getElementById('editProductStock').value = product.stock;
    document.getElementById('editProductDescription').value = product.description;
    document.getElementById('editProductImage').value = product.image;

    // Show edit modal
    const modal = new bootstrap.Modal(document.getElementById('editProductModal'));
    modal.show();
  }

  updateProduct() {
    const id = parseInt(document.getElementById('editProductId').value);
    const product = this.data.products.find(p => p.id === id);
    
    if (product) {
      product.name = document.getElementById('editProductName').value;
      product.category = document.getElementById('editProductCategory').value;
      product.price = parseFloat(document.getElementById('editProductPrice').value);
      product.stock = parseInt(document.getElementById('editProductStock').value);
      product.description = document.getElementById('editProductDescription').value;
      product.image = document.getElementById('editProductImage').value;

      this.saveToStorage('products', this.data.products);
      this.loadProducts();
      
      // Close modal
      const modal = bootstrap.Modal.getInstance(document.getElementById('editProductModal'));
      modal.hide();
      
      this.showAlert('Product updated successfully', 'success');
    }
  }

  deleteProduct(id) {
    if (confirm('Are you sure you want to delete this product?')) {
      this.data.products = this.data.products.filter(p => p.id !== id);
      this.saveToStorage('products', this.data.products);
      this.loadProducts();
      this.showAlert('Product deleted successfully', 'success');
    }
  }

  searchProducts(query) {
    if (!query) {
      this.renderProducts(this.data.products);
      return;
    }

    const filtered = this.data.products.filter(product => 
      product.name.toLowerCase().includes(query.toLowerCase()) ||
      product.category.toLowerCase().includes(query.toLowerCase())
    );
    
    this.renderProducts(filtered);
  }

  // Password Management
  changePassword() {
    const currentPassword = document.getElementById('currentPassword').value;
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (!currentPassword || !newPassword || !confirmPassword) {
      this.showAlert('Please fill in all password fields', 'danger');
      return;
    }

    if (newPassword !== confirmPassword) {
      this.showAlert('New passwords do not match', 'danger');
      return;
    }

    // In a real application, this would verify with the server
    // For now, we'll just show success
    this.showAlert('Password changed successfully', 'success');
    
    // Clear form
    document.getElementById('passwordChangeForm').reset();
  }

  // Admin Management
  addAdmin() {
    const name = document.getElementById('adminName').value;
    const username = document.getElementById('adminUsername').value;
    const email = document.getElementById('adminEmail').value;
    const password = document.getElementById('adminPassword').value;
    const role = document.getElementById('adminRole').value;

    if (!name || !username || !email || !password) {
      this.showAlert('Please fill in all required fields', 'danger');
      return;
    }

    // Store admin in localStorage (in real app, this would be server-side)
    const admins = JSON.parse(localStorage.getItem('admins') || '[]');
    const newAdmin = {
      id: Date.now(),
      name,
      username,
      email,
      role,
      createdAt: new Date().toISOString()
    };
    
    admins.push(newAdmin);
    localStorage.setItem('admins', JSON.stringify(admins));

    // Clear form
    document.getElementById('addAdminForm').reset();
    
    // Show success message
    this.showAlert('Admin added successfully!', 'success');
  }

  // Utility Functions
  getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  previewImage(file, imageNumber) {
    const previewId = imageNumber ? `imagePreview${imageNumber}` : 'imagePreview';
    const preview = document.getElementById(previewId);
    if (!file) {
      preview.innerHTML = '';
      return;
    }

    // Check file size (5MB limit)
    if (file.size > 5 * 1024 * 1024) {
      this.showAlert('Image size should not exceed 5MB', 'error');
      return;
    }

    // Check file type
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    if (!allowedTypes.includes(file.type)) {
      this.showAlert('Only JPEG, PNG, and GIF images are allowed', 'error');
      return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
      preview.innerHTML = `
        <img src="${e.target.result}" alt="Preview" style="max-width: 200px; max-height: 200px; border-radius: 8px; border: 1px solid #ddd;">
        <p class="mt-2 small text-muted">${file.name} (${(file.size / 1024).toFixed(1)} KB)</p>
      `;
    };
    reader.readAsDataURL(file);
  }

  getStatusColor(status) {
    const colors = {
      pending: 'warning',
      processing: 'info',
      shipped: 'primary',
      delivered: 'success',
      cancelled: 'danger'
    };
    return colors[status] || 'secondary';
  }

  showAlert(message, type = 'info') {
    // Remove existing alerts
    const existingAlerts = document.querySelectorAll('.alert');
    existingAlerts.forEach(alert => alert.remove());

    // Create new alert
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.style.position = 'fixed';
    alertDiv.style.top = '20px';
    alertDiv.style.right = '20px';
    alertDiv.style.zIndex = '9999';
    alertDiv.innerHTML = `
      ${message}
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    // Auto dismiss after 5 seconds
    setTimeout(() => {
      if (alertDiv.parentNode) {
        alertDiv.remove();
      }
    }, 5000);
  }

  getFromStorage(key) {
    try {
      const data = localStorage.getItem(`zetumart_admin_${key}`);
      return data ? JSON.parse(data) : null;
    } catch (error) {
      console.error(`Error loading ${key} from storage:`, error);
      return null;
    }
  }

  saveToStorage(key, data) {
    try {
      localStorage.setItem(`zetumart_admin_${key}`, JSON.stringify(data));
    } catch (error) {
      console.error(`Error saving ${key} to storage:`, error);
    }
  }

  logout() {
    if (confirm('Are you sure you want to logout?')) {
      localStorage.removeItem('zetumart_admin_token');
      window.location.href = '/admin/login/';
    }
  }

  // Chart Functions
  initChart() {
    const ctx = document.getElementById('salesChart');
    if (!ctx) return;

    this.chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Sales',
          data: [12000, 19000, 15000, 25000, 22000, 30000],
          borderColor: 'rgb(75, 192, 192)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Monthly Sales'
          }
        }
      }
    });
  }

  updateChart() {
    if (!this.chart) return;
    
    // Update with actual data
    const monthlyData = this.calculateMonthlySales();
    this.chart.data.datasets[0].data = monthlyData;
    this.chart.update();
  }

  calculateMonthlySales() {
    // Calculate sales for the last 6 months
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'];
    const currentMonth = new Date().getMonth();
    const salesData = [];
    
    for (let i = 5; i >= 0; i--) {
      const monthIndex = (currentMonth - i + 12) % 12;
      const monthOrders = this.data.orders.filter(order => {
        const orderMonth = new Date(order.date).getMonth();
        return orderMonth === monthIndex;
      });
      
      const monthSales = monthOrders.reduce((total, order) => total + order.total, 0);
      salesData.push(monthSales);
    }
    
    return salesData;
  }

  // Mock Data Generation
  generateMockProducts() {
    return [
      {
        id: 1,
        name: 'Laptop Pro 15"',
        category: 'Electronics',
        price: 89999,
        stock: 15,
        description: 'High-performance laptop with 16GB RAM and 512GB SSD',
        image: 'https://via.placeholder.com/300x300'
      },
      {
        id: 2,
        name: 'Wireless Mouse',
        category: 'Accessories',
        price: 2499,
        stock: 50,
        description: 'Ergonomic wireless mouse with long battery life',
        image: 'https://via.placeholder.com/300x300'
      },
      {
        id: 3,
        name: 'USB-C Hub',
        category: 'Accessories',
        price: 3499,
        stock: 30,
        description: '7-in-1 USB-C hub with HDMI, USB 3.0, and SD card reader',
        image: 'https://via.placeholder.com/300x300'
      },
      {
        id: 4,
        name: 'Mechanical Keyboard',
        category: 'Accessories',
        price: 6999,
        stock: 20,
        description: 'RGB mechanical keyboard with blue switches',
        image: 'https://via.placeholder.com/300x300'
      },
      {
        id: 5,
        name: 'Monitor 27"',
        category: 'Electronics',
        price: 24999,
        stock: 10,
        description: '27-inch 4K monitor with HDR support',
        image: 'https://via.placeholder.com/300x300'
      }
    ];
  }

  generateMockOrders() {
    const orders = [];
    for (let i = 1; i <= 20; i++) {
      const statuses = ['pending', 'processing', 'shipped', 'delivered'];
      const customers = ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Charlie Wilson'];
      const payments = ['M-Pesa', 'Card', 'Bank Transfer'];
      
      orders.push({
        id: 1000 + i,
        customer: customers[Math.floor(Math.random() * customers.length)],
        email: `customer${i}@example.com`,
        phone: `07${Math.floor(Math.random() * 100000000)}`,
        county: 'Nairobi',
        items: [
          {
            name: 'Sample Product',
            price: Math.floor(Math.random() * 50000) + 1000,
            quantity: Math.floor(Math.random() * 3) + 1
          }
        ],
        total: Math.floor(Math.random() * 50000) + 1000,
        payment: payments[Math.floor(Math.random() * payments.length)],
        status: statuses[Math.floor(Math.random() * statuses.length)],
        date: new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000).toISOString()
      });
    }
    return orders;
  }

  generateMockUsers() {
    const users = [];
    for (let i = 1; i <= 15; i++) {
      users.push({
        id: i,
        username: `user${i}`,
        email: `user${i}@example.com`,
        fullName: `User ${i} Name`,
        phone: `07${Math.floor(Math.random() * 100000000)}`,
        county: ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru'][Math.floor(Math.random() * 4)],
        address: `Address ${i}, Street ${i}`,
        joined: new Date(Date.now() - Math.random() * 365 * 24 * 60 * 60 * 1000).toISOString()
      });
    }
    return users;
  }

  generateMockMessages() {
    const messages = [];
    for (let i = 1; i <= 10; i++) {
      messages.push({
        id: i,
        name: `Customer ${i}`,
        email: `customer${i}@example.com`,
        subject: `Subject ${i}`,
        message: `This is a sample message from customer ${i}. Lorem ipsum dolor sit amet, consectetur adipiscing elit.`,
        read: Math.random() > 0.5,
        date: new Date(Date.now() - Math.random() * 7 * 24 * 60 * 60 * 1000).toISOString()
      });
    }
    return messages;
  }
}

// Initialize the admin dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  window.admin = new ZetuMartAdmin();
});
